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
          <el-button @click="handleClick(scope.row)" size="small" type="primary" round>查看</el-button>
          <el-button @click="handleClick(scope.row)" size="small" type="danger" round>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {BookModel} from "@/models/category";
import {getBookList} from "@/http/api";

export default defineComponent({
  name: "BookList",
  setup() {
    const book_list = ref<BookModel[]>([])
    const handleClick = () => {

    }
    getBookList().then((res: BookModel[] | any) =>{
      book_list.value = res
    })
    return {
      book_list,
      handleClick
    }
  }
})
</script>

<style scoped>

</style>
