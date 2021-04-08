<template>
  <div>
    <el-table :data="book_list" border style="width: 100%">
      <el-table-column prop="book_name" label="书籍名称" />
      <el-table-column prop="author_name" label="作者" />
      <el-table-column prop="cate_name" label="所属分类" width="80" />
      <el-table-column prop="channel_name" label="来源" width="80" />
      <el-table-column prop="chapter_num" label="章节数" width="100" />
      <el-table-column prop="cover" label="封面图片" width="100">
        <template #default="scope">
          <img :src="scope.row.cover" style="width: 60px;height: 60px;">
        </template>
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="160">
        <template #default="scope">
          <el-button size="small" type="primary" round @click="handleLook(scope.$index, scope.row)">查看</el-button>
          <el-button size="small" type="danger" round @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {BookModel} from "@/models/models";
import {getBookList} from "@/http/api";
import {useRouter} from "vue-router";

export default defineComponent({
  name: "BookList",
  setup() {
    const router = useRouter()
    const book_list = ref<BookModel[]>([])
    const handleLook = (index: number, book: BookModel) => {
      router.push({path: `/book/detail?id=${book.book_id}`})
    }
    const handleDelete = (index: number, book: BookModel) => {

    }
    getBookList().then((res: BookModel[] | any) =>{
      book_list.value = res
    })
    return {
      book_list,
      handleLook,
      handleDelete
    }
  }
})
</script>

<style scoped>

</style>
