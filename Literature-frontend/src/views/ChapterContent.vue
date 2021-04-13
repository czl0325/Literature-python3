<template>
  <navigation-bar title="章节详情"/>
  <div class="my-container">
    <p>{{ chapter.chapter_name }}</p>
    <div v-html="chapter.content"></div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";
import {ChapterModel} from "@/models/models";

export default defineComponent({
  name: "ChapterContent",
  components: {NavigationBar},
  setup() {
    const chapter = ref<ChapterModel>({})
    return {
      chapter
    }
  }
})
</script>

<style scoped>

</style>
