import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import Sanford from "@/components/Sanford"
import UserCenter from '@/components/user/Center'
import UserLogin from '@/components/Login'
import UserRegister from "@/components/Register"

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
      component: Home,
      children: [
        {
          path: '/home/login',
          name: 'UserLogin',
          component: UserLogin
        },
        {
          path: '/home/register',
          name: 'UserRegister',
          component: UserRegister
        },
      ]
    },
    {
      path: '/sanford',
      name: 'Sanford',
      component: Sanford,
      children: [
        {
          path: '/sanford/hot',
          name: 'SanfordHot',
          component: Hot
        },
        {
          path: '/sanford/user/center',
          name: 'UserCenter',
          component: UserCenter
        },
      ]
    },
  ],
  mode: "history",
})
