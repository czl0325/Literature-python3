<template>
  <div>
    <el-form :model="chapter" label-width="80px">
      <el-form-item label="章节id">
        <el-input v-model="chapter.chapter_id" />
      </el-form-item>
      <el-form-item label="章节名称">
        <el-input v-model="chapter.chapter_name" />
      </el-form-item>
      <el-form-item label="章节内容">
        <el-input v-model="chapter.content" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAddChapter">{{ chapter.chapter_id ? '更新章节' : '立即添加' }}</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {ChapterModel} from "@/models/models";
import {useRoute} from "vue-router";
import {addChapter} from "@/http/api";
import {ElMessage} from "element-plus";

export default defineComponent({
  name: "ChapterAdd",
  setup() {
    const route = useRoute()
    const book_id = route.query.book_id
    const c_id = route.query.c_id
    const chapter = ref<ChapterModel>({})
    if (typeof book_id === 'string') {
      chapter.value.book_id = parseInt(book_id)
    }
    if (typeof c_id === 'string') {
      chapter.value.id = parseInt(c_id)
    }
    const onAddChapter = () => {
      if (typeof book_id === 'string' && book_id.length > 0) {
        addChapter(chapter.value).then(() => {
          ElMessage.success('添加章节成功!')
          if (!chapter.value.chapter_id) {
            chapter.value = {}
          }
        })
      } else {
        ElMessage.error('缺少书籍id')
      }
    }
    return {
      chapter,
      onAddChapter
    }
  }
})
</script>

<style scoped>

</style>
