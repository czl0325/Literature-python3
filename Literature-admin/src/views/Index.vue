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
      <el-menu>
        <template v-for="menu in menus" >
          <el-submenu v-if="menu.child" :key="menu.path" :index="menu.index">
            <template #title>分类</template>
            <el-menu-item v-for="subMenu in menu.child" :key="subMenu.path" :index="subMenu.path">{{ subMenu.title }}</el-menu-item>
          </el-submenu>
          <el-menu-item v-else :key="menu.path" :index="menu.path">首页</el-menu-item>
        </template>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <div>
        <div class="view-nav">
          <el-tabs v-model="act" type="card" closable>
            <el-tab-pane label="首页"></el-tab-pane>
            <el-tab-pane label="分类"></el-tab-pane>
          </el-tabs>
          <transition name="display">
            <keep-alive>
              <router-view />
            </keep-alive>
          </transition>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {menuList} from '../data/menu'

export default defineComponent({
  name: "Index",
  setup() {
    const act = ref(0)
    const menus = ref(menuList)
    return {
      act,
      menus
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
