<template>
  <navigation-bar title="注册" left-text="返回" fixed border left-arrow ></navigation-bar>

</template>

<script lang="ts">
import {defineComponent} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";

export default defineComponent ({
  name: "Register",
  components: {
    NavigationBar
  },
  setup() {

    return {

    }
  }
})
</script>

<style scoped>

</style>
