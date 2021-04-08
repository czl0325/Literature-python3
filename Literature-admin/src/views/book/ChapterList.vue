<template>
  <div>
    <el-table :data="chapter_list" border style="width: 100%">
      <el-table-column prop="chapter_id" label="章节" width="150"/>
      <el-table-column prop="chapter_name" label="标题" />
    </el-table>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {useRoute} from "vue-router";
import {getChapterList} from "@/http/api";
import {ChapterModel} from "@/models/models";

export default defineComponent({
  name: "ChapterList",
  setup() {
    const route = useRoute()
    const chapter_list = ref<ChapterModel[]>([])
    const book_id = route.query.id
    if (typeof book_id === 'string') {
      getChapterList(parseInt(book_id)).then((res:ChapterModel|any) => {
        chapter_list.value = res
      })
    }
    return {
      chapter_list
    }
  }
})
</script>

<style scoped>

</style>
