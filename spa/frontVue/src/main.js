import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'
import VueCookie from 'vue-cookie'
import App from './App.vue'
import event from './components/Event.vue'
import Hello from './components/Hello.vue'

Vue.use(Router)
Vue.use(Meta)
Vue.use(VueCookie)

const router = new Router({
 routes: [
   {
     path: '/',
     name:'home',
     component: Hello,
   },
   {
     path: '/event/:id',
     name:'event',
     component: event,
     props: true,
   },
 ],
  mode: 'history'
})

new Vue({
 el: '#app',
 render: h => h(App),
 router
})