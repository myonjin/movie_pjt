import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import DetailView from '../views/DetailView.vue'
import SearchView from '../views/SearchView.vue'
import LoginViewtest from '../views/LoginViewtest.vue'
import ProfileView from '@/views/ProfileView'
import CommunityView from '../views/CommunityView'
import CreateView from '../views/CreateView'
import ArticleDetailView from '../views/ArticleDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginViewtest
  },
  {
    path: '/home',
    name: 'home',
    component: MainView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path:'/community',
    name: 'community',
    component: CommunityView
  },
  {
    path:'/create',
    name: 'create',
    component: CreateView
  },
   { path: '/detail/:id',
    name: 'articledetail',
    component: ArticleDetailView
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
