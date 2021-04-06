import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import Index from '../views/Index.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', redirect: '/home' },
  { path: '/', name: 'Index', component: Index, children: [
      { path: '/home', name: '首页', component: ()=>import('../views/Home.vue') },
      { path: '/category/list', name: '分类列表', component: ()=>import('../views/category/CategoryList.vue') },
      { path: '/category/add', name: '添加分类', component: ()=>import('../views/category/CategoryAdd.vue') },
    ] }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
