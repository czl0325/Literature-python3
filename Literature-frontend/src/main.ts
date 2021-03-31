import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/router";

import 'vant/lib/index.less'

import {Tabbar, TabbarItem} from 'vant'

const app = createApp(App)
app.use(router)
app.use(Tabbar).use(TabbarItem)
app.mount('#app')
