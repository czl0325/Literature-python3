<template>
  <div style="padding: 30px 0; box-sizing: border-box;">
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
      <el-form-item v-if="book.book_id" label="渠道名">
        <el-input v-model="book.channel_name" />
      </el-form-item>
      <el-form-item v-if="book.book_id" label="爬取网址">
        <el-input v-model="book.channel_url" />
      </el-form-item>
      <el-form-item v-if="book.book_id" label="短描述">
        <el-input v-model="book.short_des" type="textarea" />
      </el-form-item>
      <el-form-item v-if="book.book_id" label="章节数">
        <el-input v-model="book.chapter_num" disabled />
      </el-form-item>
      <el-form-item v-if="book.book_id" label="热度">
        <el-input v-model="book.heat" disabled />
      </el-form-item>
      <el-form-item v-if="book.book_id" label="收藏数">
        <el-input v-model="book.collect_count" disabled />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAddBook">{{ book.book_id ? '更新书籍' : '立即添加' }}</el-button>
        <el-button v-if="book.book_id" type="primary" @click="toChapterList">查看章节</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {BookModel, CategoryModel} from "@/models/models";
import {getCategoryList, addBook, getBookDetail} from "@/http/api";
import {ElMessage} from "element-plus";
import {useRoute, useRouter} from "vue-router";
export default defineComponent({
  name: "BookAdd",
  setup() {
    const route = useRoute()
    const router = useRouter()
    const book = ref<BookModel|any>({})
    const categories = ref<CategoryModel[]>([])
    getCategoryList().then((res:CategoryModel[]|any)=>{
      categories.value = res
    })
    const onSelectCategory = (id: string) => {
      book.value.cate_id = id
    }
    let book_id = route.query.id
    if (typeof book_id === 'string') {
      getBookDetail(parseInt(book_id)).then((res:BookModel|any)=>{
        book.value = res
      })
    }
    const onAddBook = () => {
      addBook(book.value).then((res:BookModel|any)=>{
        ElMessage.success('书籍添加成功!')
        book.value = {}
      })
    }
    const toChapterList = () => {
      router.push({ path: '/book/chapter/list', query: {id: book.value.book_id}})
    }
    return {
      book,
      categories,
      onSelectCategory,
      onAddBook,
      toChapterList
    }
  }
})
</script>

<style scoped>

</style>
