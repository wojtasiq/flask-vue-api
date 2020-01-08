import Vue from 'vue'
import App from './App.vue'
import router from './services/router'
import vuetify from './services/vuetify';

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  vuetify,
  components: { App }
}).$mount('#app')
