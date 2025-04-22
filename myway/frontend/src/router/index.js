import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomePage.vue'
import Catalogue from '../components/CataloguePage.vue'
import AboutUs from '../components/AboutUsPage.vue'
import CarDetail from '../components/CarDetail.vue';
import Login from '../components/LoginPage.vue'
import Register from '../components/RegisterPage.vue'
import store from '../store/index.js'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/catalogue',
    name: 'Catalogue',
    component: Catalogue
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: AboutUs
  },
  {
    path: '/cars/:id',
    name: 'CarDetail',
    component: CarDetail,
    props: true,
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: Login,
    meta: { guestOnly: true }
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: Register,
    meta: { guestOnly: true }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login')
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.guestOnly)) {
    if (isAuthenticated) {
      next('/')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router