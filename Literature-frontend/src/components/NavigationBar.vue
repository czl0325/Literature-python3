<template>
  <van-nav-bar @click-left="onBack" left-text="返回" fixed border left-arrow  v-bind="$attrs"></van-nav-bar>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import {useRouter} from "vue-router";

export default defineComponent ({
  name: "NavigationBar",
  inheritAttrs: false,
  setup() {
    const router = useRouter()
    const onBack = () => {
      router.back()
    }
    return {
      onBack
    }
  }
})
</script>

<style scoped>

</style>
