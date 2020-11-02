import Vue from 'vue'
// import './plugins/element.js'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.devtools = true;

new Vue({
   store,
   router,
   render: h => h(App),
  }).$mount('#app')
  