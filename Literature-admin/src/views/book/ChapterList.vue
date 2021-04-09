<template>
  <div>
    <div style="text-align: right;padding: 5px 0;box-sizing: border-box;">
      <el-button type="primary" @click="toChapter">添加章节</el-button>
    </div>
    <el-table :data="chapter_list" border style="width: 100%">
      <el-table-column prop="chapter_id" label="章节" width="150"/>
      <el-table-column prop="chapter_name" label="标题" />
      <el-table-column fixed="right" label="操作" width="100">
        <template #default="scope">
          <el-button size="small" type="primary" round @click="toChapter(scope.$index, scope.row)">编辑章节</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {useRoute, useRouter} from "vue-router";
import {getChapterList} from "@/http/api";
import {ChapterModel} from "@/models/models";
import {ElMessage} from "element-plus";

export default defineComponent({
  name: "ChapterList",
  setup() {
    const route = useRoute()
    const router = useRouter()
    const chapter_list = ref<ChapterModel[]>([])
    const book_id = route.query.id
    if (typeof book_id === 'string') {
      getChapterList(parseInt(book_id)).then((res:ChapterModel|any) => {
        chapter_list.value = res
      })
    }
    const toChapter = (index: number, chapter: ChapterModel) => {
      if (!book_id) {
        ElMessage.error('书籍信息错误')
        return;
      }
      router.push( { path: '/book/chapter/add', query: { book_id: book_id, chapter_id:  chapter.chapter_id } } )
    }
    return {
      chapter_list,
      toChapter
    }
  }
})
</script>

<style scoped>

</style>
