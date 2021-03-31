<template>
  <router-view></router-view>
  <van-tabbar v-model="active" active-color="#ee0a24" inactive-color="#000" v-show="route.meta.showTab">
    <van-tabbar-item icon="wap-home">首页</van-tabbar-item>
    <van-tabbar-item icon="label">分类</van-tabbar-item>
    <van-tabbar-item icon="manager">我的</van-tabbar-item>
  </van-tabbar>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRoute } from "vue-router";

export default defineComponent({
  name: 'App',
  components: {

  },
  setup() {
    const active = ref(0)
    const route = useRoute()

    return {
      active,
      route
    }
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
