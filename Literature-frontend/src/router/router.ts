import {createRouter, createWebHashHistory} from "vue-router";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {path: '/', redirect: '/home'},
    {path:'/home', name: 'home', component: ()=>import('@/views/home/Home.vue'), meta: {showTab: true, num: 0}},
    {path:'/category', name: 'category', component: ()=>import('@/views/category/Category.vue'), meta: {showTab: true, num: 1}},
    {path:'/me', name: 'me', component: ()=>import('@/views/me/Me.vue'), meta: {showTab: true, num: 2}},
    {path:'/login', name: 'login', component: ()=>import('@/views/login/Login.vue')},
    {path:'/register', name: 'register', component: ()=>import('@/views/login/Register.vue')},

    {path:'/books', name: 'books', component: ()=>import('@/views/category/Books.vue')},
    {path:'/chapter', name: 'chapter', component: ()=>import('@/views/category/ChapterList.vue')},
    {path:'/content', name: 'content', component: ()=>import('@/views/category/ChapterContent.vue')},

    {path:'/mybooks', name: 'mybooks', component: ()=>import('@/views/me/MyBooks.vue')},
  ]
})

export default router
