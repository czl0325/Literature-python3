<template>
  <el-row class="nav">
    <el-col :span="6">
      <div class="logo">LOGO</div>
    </el-col>
    <el-col :span="18" style="text-align: right">

    </el-col>
  </el-row>
  <el-row style="height: 100%;">
    <el-col :span="4">
      <el-menu :default-active="active_path">
        <template v-for="menu in menus">
          <el-submenu v-if="menu.child" :key="menu.path" :index="menu.path">
            <template #title>分类</template>
            <el-menu-item v-for="subMenu in menu.child" :key="subMenu.path" :index="subMenu.path" @click="menuClick(subMenu)">{{ subMenu.title }}
            </el-menu-item>
          </el-submenu>
          <el-menu-item v-else :key="menu.path" :index="menu.path" @click="menuClick(menu)">首页</el-menu-item>
        </template>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <div>
        <div class="view-nav">
          <el-tabs v-model="active_path" type="card" closable @tab-click="tabClick" @tab-remove="tabRemove">
            <el-tab-pane v-for="tab in tabs" :name="tab.path" :key="tab.path" :label="tab.title"></el-tab-pane>
          </el-tabs>
          <router-view />
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script lang="ts">
import {defineComponent, ref, watch, onMounted} from 'vue'
import {menuList} from '../data/menu'
import {useRouter, useRoute} from "vue-router";
import {useStore} from "vuex";

interface MenuModel {
  name: string,
  title: string,
  path: string,
  child?: MenuModel[]
}

interface TabModel {
  title: string,
  path: string
}

export default defineComponent({
  name: "Index",
  setup() {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()
    const active_path = ref('/home')
    const menus = ref<MenuModel[]>(menuList)
    const tabs = ref<TabModel[]>(store.state.tabs)

    const menuClick = (menu: MenuModel) => {
      router.push({path: menu.path||'/'})
      tabs.value.push({title: menu.title, path: menu.path})
      tabs.value = sort(tabs.value)
      store.commit('updateTabs', tabs.value)
    }
    const tabClick = (tab: any) => {
      router.push({path: tab.paneName})
    }
    const tabRemove = (path: string) => {
      tabs.value.forEach((item, index) =>{
        if((item.path == path) && index>0) {
          if(active_path.value == path){
            active_path.value = tabs.value[index-1].path;
            router.push({path: active_path.value})
          }
          tabs.value.splice(index,1)
          store.commit('updateTabs', tabs.value)
        }
      })
    }
    const sort = (arr: TabModel[]) => {
      let temp = arr.map((item) => {
        return JSON.stringify(item);
      });
      temp = Array.from(new Set(temp));
      return temp.map((item) => {
        return JSON.parse(item);
      });
    }
    watch(()=>route.path, (val) => {
      active_path.value = route.path
    }, {immediate: true})
    return {
      active_path,
      menus,
      tabs,
      menuClick,
      tabClick,
      tabRemove
    }
  }
})
</script>

<style lang="less" scoped>
.nav {
  background-color: #ddd;
  width: 100%;
  height: 60px;
  line-height: 60px;
  padding: 5px 10px;
  box-sizing: border-box;

  .logo {
    width: 80%;
    height: 100%;
    line-height: 50px;
    background-color: #42b983;
    color: white;
  }
}

.view-nav {
  background-color: #fff;
  margin: 5px 10px;
  padding: 7px 10px;
  border-radius: 4px;;
  height: 40px;
}
</style>
