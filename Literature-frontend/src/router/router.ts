import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {path: '/', redirect: '/home'},
    {path:'/home', name: 'home', component: ()=>import('@/views/Home.vue'), meta: {showTab: true, num: 0}},
    {path:'/category', name: 'category', component: ()=>import('@/views/Category.vue'), meta: {showTab: true, num: 1}},
    {path:'/me', name: 'me', component: ()=>import('@/views/Me.vue'), meta: {showTab: true, num: 2}},
    {path:'/login', name: 'login', component: ()=>import('@/views/Login.vue')},
    {path:'/register', name: 'register', component: ()=>import('@/views/Register.vue')},

    {path:'/books', name: 'books', component: ()=>import('@/views/Books.vue')},
    {path:'/chapter', name: 'chapter', component: ()=>import('@/views/ChapterList.vue')},
    {path:'/content', name: 'content', component: ()=>import('@/views/ChapterContent.vue')}
  ]
})

export default router
