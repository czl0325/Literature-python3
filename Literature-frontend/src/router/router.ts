import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {path: '/', redirect: '/home'},
    {path:'/home', name: 'home', component: ()=>import('@/views/Home.vue'), meta: {showTab: true}},
    {path:'/category', name: 'category', component: ()=>import('@/views/Category.vue'), meta: {showTab: true}},
    {path:'/me', name: 'me', component: ()=>import('@/views/Me.vue'), meta: {showTab: true}}
  ]
})

export default router
