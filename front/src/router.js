import Vue from 'vue'
import Router from 'vue-router'
import Start from './views/start.vue'
import Result from './views/result.vue'
// import App from './App.vue'

Vue.use(Router)

export default new Router({
    base: process.env.BASE_URL,
    mode: 'history',
    routes: [
        // {
        // path: '/',
        // name: 'app',
        // component: App
        // },    
        {
        path: '/views/start',
        name: 'start',
        component: Start
        },
        {
        path: '/views/result',
        name: 'result',
        component: Result
        }        
    ]
})