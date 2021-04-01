import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/router";
import store from '@/store/index';

import 'vant/lib/index.less'
import "./css/common.less";

import {Tabbar, TabbarItem, NavBar, Cell, CellGroup, Field, Form, Button} from 'vant'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(Tabbar).use(TabbarItem).use(NavBar).use(Cell).use(CellGroup).use(Field).use(Form).use(Button)
app.mount('#app')
