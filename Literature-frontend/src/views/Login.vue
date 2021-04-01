<template>
  <van-nav-bar title="登录" left-text="返回" fixed border left-arrow @click-left="onBack" />
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import {useRouter} from "vue-router";

export default defineComponent({
  name: "Login",
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
