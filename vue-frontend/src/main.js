import Vue from 'vue'
import App from './App.vue'
import router from './services/router'
import vuetify from './services/vuetify';
import store from './store/store';
import Axios from 'axios'

Vue.prototype.$http = Axios;

const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = "Bearer " + token
}

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  store,
  vuetify,
  components: { App }
}).$mount('#app')
