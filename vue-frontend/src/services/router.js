import Vue from 'vue';
import Router from 'vue-router';
import HomePage from "../components/home-page";
import LoginPage from "../components/login-page";
import store from '../store/store'

Vue.use(Router);

export const router = new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: HomePage },
        { path: '/login', component: LoginPage },
        { path: '/*', redirect: '/' }
    ]
});

router.beforeEach((to,from, next) => {
    const loginPage = '/login'

    if(to.path !== loginPage){
        if (store.getters.isLoggedIn){
            return next()
        }
        return next(loginPage)
    }else {
        return next()
    }
});

export default router
