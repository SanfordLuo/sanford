import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Hot from '@/components/Hot'
import Sanford from "@/components/Sanford"
import UserCenter from '@/components/user/Center'
import UserLogin from '@/components/user/Login'
import UserRegister from '@/components/user/Register'
import Test from '@/components/Test'
import Test1 from '@/components/UploadAvatarDemo'
import Test2 from '@/components/UploadAvatar'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
    {
      path: '/test1',
      name: 'Test1',
      component: Test1,
    },
    {
      path: '/test2',
      name: 'Test2',
      component: Test2,
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
