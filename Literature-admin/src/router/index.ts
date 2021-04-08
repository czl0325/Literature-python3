import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Index from '../views/Index.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/home' },
  { path: '/', name: 'Index', component: Index, children: [
      { path: '/home', name: 'Home', component: ()=>import('../views/Home.vue') },
      { path: '/category/list', name: 'CategoryList', component: ()=>import('../views/category/CategoryList.vue') },
      { path: '/category/add', name: 'CategoryAdd', component: ()=>import('../views/category/CategoryAdd.vue') },
      { path: '/book/list', name: 'BookList', component: ()=>import('../views/book/BookList.vue') },
      { path: '/book/add', name: 'BookAdd', component: ()=>import('../views/book/BookAdd.vue') },
      { path: '/book/chapter/list', name: 'ChapterList', component: ()=>import('../views/book/ChapterList.vue') },
      { path: '/book/chapter/add', name: 'ChapterAdd', component: ()=>import('../views/book/ChapterAdd.vue') }
    ] }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
