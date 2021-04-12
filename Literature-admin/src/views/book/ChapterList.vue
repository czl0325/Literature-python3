<template>
  <div>
    <div style="text-align: right;padding: 5px 0;box-sizing: border-box;display: flex;
justify-content: space-between;align-items: center;" >
      <el-button type="primary" @click="toChapter">添加章节</el-button>
      <div style="height: 40px;line-height: 40px;margin-bottom: 5px;">
        <span>跳转到第</span>
        <el-input v-model="pageNum" type="number" style="display: inline-block;width: 100px;height: 40px;margin: 0 5px;" />
        <span>页</span>
        <el-button type="primary" style="margin-left: 10px;" @click="requestChapterList">跳转</el-button>
      </div>
    </div>
    <el-table :data="chapter_page.items" border style="width: 100%">
      <el-table-column prop="chapter_id" label="章节" width="150"/>
      <el-table-column prop="chapter_name" label="标题" />
      <el-table-column fixed="right" label="操作" width="100">
        <template #default="scope">
          <el-button size="small" type="primary" round @click="toChapter(scope.row)">编辑章节</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination background layout="prev, pager, next" :total="chapter_page.total_num" :page-size="20" :current-page="parseInt(pageNum)" @current-change="onPageChange" />
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {useRoute, useRouter} from "vue-router";
import {getChapterList} from "@/http/api";
import {ChapterModel, PageModel} from "@/models/models";
import {ElMessage} from "element-plus";

export default defineComponent({
  name: "ChapterList",
  setup() {
    const route = useRoute()
    const router = useRouter()
    const chapter_page = ref<PageModel<ChapterModel>>({})
    const book_id = route.query.id
    const pageNum = ref(1)
    const requestChapterList = () => {
      if (typeof book_id === 'string') {
        getChapterList(parseInt(book_id), pageNum.value).then((res:PageModel<ChapterModel>|any) => {
          chapter_page.value = res
        })
      }
    }
    requestChapterList()
    const toChapter = (chapter: ChapterModel) => {
      if (!book_id) {
        ElMessage.error('书籍信息错误')
        return;
      }
      if (chapter) {
        router.push( { path: '/book/chapter/add', query: { id: chapter.id } } )
      } else {
        router.push( { path: '/book/chapter/add', query: { book_id: book_id } } )
      }
    }
    const onPageChange = (page: number) => {
      pageNum.value = page
      requestChapterList()
    }
    return {
      pageNum,
      chapter_page,
      toChapter,
      onPageChange,
      requestChapterList
    }
  }
})
</script>

<style lang="less" scoped>
.pagination {
  width: 100%;
  padding: 20px 0;
  box-sizing: border-box;
  text-align: right;
}
</style>
