import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import Sanford from "@/components/Sanford"
import UserCenter from '@/components/user/Center'
import UserLogin from '@/components/user/Login'
import UserRegister from "@/components/user/Register"

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
    {
      path: '/sanford/user/login',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path: '/sanford/user/register',
      name: 'UserRegister',
      component: UserRegister
    },
  ],
  mode: "history",
})
