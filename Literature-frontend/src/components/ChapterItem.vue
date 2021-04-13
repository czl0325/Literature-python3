<template>
  <div class="item-container" style="height: 50px;justify-content: center;" @click="toChapterContent">
    <span>{{ chapter.chapter_name }}</span>
  </div>
</template>

<script lang="ts">
import {defineComponent, PropType, ref} from 'vue'
import {ChapterModel} from "@/models/models";

export default defineComponent({
  name: "ChapterItem",
  props: {
    chapter: {
      type: Object as PropType<ChapterModel>,
      default: {}
    }
  },
  setup() {
    const toChapterContent = () => {

    }
    return {
      toChapterContent
    }
  }
})
</script>

<style scoped>

</style>
