import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomePage.vue'
import Catalogue from '../components/CataloguePage.vue'
import AboutUs from '../components/AboutUsPage.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router