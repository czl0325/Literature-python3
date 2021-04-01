<template>
  <router-view></router-view>
  <van-tabbar v-model="route.meta.num" active-color="#ee0a24" inactive-color="#000" v-show="route.meta.showTab" safe-area-inset-bottom>
    <van-tabbar-item to="home" icon="wap-home">书城</van-tabbar-item>
    <van-tabbar-item to="category" icon="label">分类</van-tabbar-item>
    <van-tabbar-item to="me" icon="manager">我的</van-tabbar-item>
  </van-tabbar>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRoute } from "vue-router";

export default defineComponent({
  name: 'App',
  components: {

  },
  setup() {
    const route = useRoute()
    return {
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
}
</style>
