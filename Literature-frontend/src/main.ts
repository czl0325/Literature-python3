import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router/router";
import store from '@/store/index';

import 'vant/lib/index.less';
import './css/common.less';
import './css/reset.css';

import {Tabbar, TabbarItem, NavBar, Cell, CellGroup, Field, Form, Button, RadioGroup, Radio, Area, Popup, Uploader, Grid, GridItem, PullRefresh, List, Search } from 'vant'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(Tabbar).use(TabbarItem).use(NavBar).use(Cell).use(CellGroup).use(Field).use(Form).use(Button).use(RadioGroup).use(Radio).use(Area).use(Popup).use(Uploader).use(Grid).use(GridItem).use(PullRefresh).use(List).use(Search)

app.mount('#app')
