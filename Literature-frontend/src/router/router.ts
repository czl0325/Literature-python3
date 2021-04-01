import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {path: '/', redirect: '/home'},
    {path:'/home', name: 'home', component: ()=>import('@/views/Home.vue'), meta: {showTab: true, num: 0}},
    {path:'/category', name: 'category', component: ()=>import('@/views/Category.vue'), meta: {showTab: true, num: 1}},
    {path:'/me', name: 'me', component: ()=>import('@/views/Me.vue'), meta: {showTab: true, num: 2}}
  ]
})

export default router
