<template>
  <div class="item-container" style="height: 50px;justify-content: center;" @click="toChapterContent">
    <span>{{ chapter.chapter_name }}</span>
  </div>
</template>

<script lang="ts">
import {defineComponent, PropType, ref} from 'vue'
import {ChapterModel} from "@/models/models";
import {useRouter} from "vue-router";
import {Toast} from "vant";

export default defineComponent({
  name: "ChapterItem",
  props: {
    chapter: {
      type: Object as PropType<ChapterModel>,
      default: {}
    }
  },
  setup(props) {
    const router = useRouter()
    const toChapterContent = () => {
      const id = props.chapter.id
      if (id) {
        router.push({path: `/content`, query: {id: id}})
      } else {
        Toast.fail('缺少章节id')
      }
    }
    return {
      toChapterContent
    }
  }
})
</script>

<style scoped>

</style>
