<template>
  <div>
    <el-form :model="book" label-width="80px">
      <el-form-item label="书籍名称">
        <el-input v-model="book.book_name" />
      </el-form-item>
      <el-form-item label="所属分类">
        <el-select v-model="book.cate_name" placeholder="请选择所属分类" style="width: 100%;" @change="onSelectCategory">
          <el-option v-for="cate in categories" :key="cate.cate_id" :label="cate.cate_name" :value="cate.cate_id" />
        </el-select>
      </el-form-item>
      <el-form-item label="作者">
        <el-input v-model="book.author_name" />
      </el-form-item>
      <el-form-item label="简介">
        <el-input v-model="book.intro" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAddBook">立即添加</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {BookModel, CategoryModel} from "@/models/models";
import {getCategoryList, addBook} from "@/http/api";
import {ElMessage} from "element-plus";

export default defineComponent({
  name: "BookAdd",
  setup() {
    const book = ref<BookModel|any>({})
    const categories = ref<CategoryModel[]>([])
    getCategoryList().then((res:CategoryModel[]|any)=>{
      categories.value = res
    })
    const onSelectCategory = (id: string) => {
      book.value.cate_id = id
    }
    const onAddBook = () => {
      addBook(book.value).then((res:BookModel|any)=>{
        ElMessage.success('书籍添加成功!')
        book.value = {}
      })
    }
    return {
      book,
      categories,
      onSelectCategory,
      onAddBook
    }
  }
})
</script>

<style scoped>

</style>
