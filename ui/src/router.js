import Vue from 'vue'
import Router from 'vue-router'
import DonateFrom from './views/DonateFrom.vue'
import DonateTo from './views/DonateTo.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'root',
      component: DonateFrom
    },
    {
      path: '/donate-from',
      name: 'donate-from',
      component: DonateFrom
    },
    {
      path: '/donate-to',
      name: 'donate-to',
      component: DonateTo
    }
  ]
})
