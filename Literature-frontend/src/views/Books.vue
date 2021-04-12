<template>
  <navigation-bar :title="cate_name"/>
  <div class="my-container">
    <van-pull-refresh style="width: 100%;min-height: 100vh;">
      <van-list>
        <div v-for="book in books" :key="book.book_id" class="item-container">
          <h2>{{ book.book_name }}</h2>
          <span>作者：{{ book.author_name }}</span>
          <span>章节数：{{ book.chapter_num }}</span>
        </div>
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {getBookList} from "@/http/api";
import {useRoute} from "vue-router";
import {BookModel} from "@/models/models";
import NavigationBar from "@/components/NavigationBar.vue";

export default defineComponent({
  name: "Books",
  components: {
    NavigationBar
  },
  setup() {
    const route = useRoute()
    const cate_id = (route.query.cate_id || '')
    const cate_name = ref('')
    const books = ref<BookModel[]>([])
    // @ts-ignore
    getBookList(cate_id).then((res:BookModel[]|any)=>{
      books.value = res
    })
    return {
      books,
      cate_name
    }
  }
})
</script>

<style lang="less" scoped>

</style>
