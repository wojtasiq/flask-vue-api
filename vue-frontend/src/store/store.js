import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user: null
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token) {
            state.status = 'success'
            state.token = token
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
            state.user = null
        },
        userData_success(state, user){
            state.user = user
            window.console.log(state.user)
        },
        userData_error(state){
            state.user = null
        }
    },
    actions: {
        login({commit}, userData) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios.post('http://127.0.0.1:5000/login',
                    {username: userData.username, password: userData.password},
                    {headers: {'content-type': 'application/json'}},
                )
                    .then(resp => {
                        window.console.log(resp)
                        const token = resp.data.token
                        localStorage.setItem('token', token)
                        axios.defaults.headers.common['Authorization'] = "Bearer " + token
                        commit('auth_success', token)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        logout({commit}) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
        userData({commit}){
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios.get('http://127.0.0.1:5000/auth/user/me',
                    {headers: {'content-type': 'application/json'}},
                )
                    .then(resp => {
                        window.console.log(resp)
                        const user = resp.data.user
                        commit('userData_success', user)
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('userData_error')
                        reject(err)
                    })
            })
        }
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
        userData: state => state.user
    }
})
