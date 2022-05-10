import Vue from 'vue'
import VueRouter from 'vue-router'
import MyLunch from '../views/MyLunch.vue'
import LottoView from '../views/LottoView.vue'
import DogView from '../views/DogView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'Mylunch',
    component: MyLunch
  },
  {
    path: '/lotto/:num',
    name: 'LottoView',
    component: LottoView
  },
  {
    path: '/dog',
    name: 'DogView',
    component: DogView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
