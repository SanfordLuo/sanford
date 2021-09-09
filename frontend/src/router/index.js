import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import User from '@/components/User'
import Login from '@/components/Login'
import Register from "@/components/Register"
import Sanford from "@/components/Sanford"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/sanford',
      name: 'Sanford',
      component: Sanford
    },
    {
      path: '/sanford/hot',
      name: 'Hot',
      component: Hot
    },
    {
      path: '/sanford/user',
      name: 'User',
      component: User
    },
    {
      path: '/sanford/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/sanford/register',
      name: 'Register',
      component: Register
    },
  ],
  mode: "history",
})
