import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import Sanford from "@/components/Sanford"
import UserCenter from '@/components/user/Center'
import UserLogin from '@/components/Login'
import UserRegister from '@/components/Register'
import Test from '@/components/Test'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
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

export default router

router.beforeEach((to, from, next) => {
  console.log(localStorage)
  let token = localStorage.getItem('token');

  if (token === null) {
    localStorage.removeItem('username')
    if (to.path === '/home' || to.path === '/home/login' || to.path === '/home/register') {
      next();
    } else {
      next('/home')
    }
  } else {
    if (to.path === '/home/login' || to.path === '/home/register') {
      next('/sanford');
    } else {
      next();
    }
  }
})
