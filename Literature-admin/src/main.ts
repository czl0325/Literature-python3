import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import 'element-plus/lib/theme-chalk/index.css'
// @ts-ignore
import { ElRow, ElCol, ElMenu, ElMenuItem, ElMenuItemGroup, ElSubmenu, ElTabs, ElTabPane, ElTable, ElTableColumn, ElButton, ElForm, ElFormItem, ElInput, ElUpload, ElIcon, ElSelect, ElOption, ElPagination } from 'element-plus'
import { ElMessage } from 'element-plus'

import './css/reset.css'

const app = createApp(App)
const components = [ ElRow, ElCol, ElMenu, ElMenuItem, ElMenuItemGroup, ElSubmenu, ElTabs, ElTabPane, ElTable, ElTableColumn, ElButton, ElForm, ElFormItem, ElInput, ElUpload, ElIcon, ElSelect, ElOption, ElPagination ]
const plugins = [ ElMessage ]
components.forEach(component => {
  app.component(component.name, component)
})
plugins.forEach(plugin => {
  app.use(plugin)
})
app.use(store).use(router).mount('#app')
