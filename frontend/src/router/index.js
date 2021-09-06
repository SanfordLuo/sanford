import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import User from '@/components/User'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/hot',
      name: 'Hot',
      component: Hot
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
  ]
})
