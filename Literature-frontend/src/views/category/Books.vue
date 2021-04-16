<template>
  <navigation-bar :title="cate_name"/>
  <div class="my-container">
    <van-pull-refresh style="width: 100%;min-height: 100vh;" v-model="state.refreshing" @refresh="requestBookList(true)">
      <van-search v-model="search_word" placeholder="请输入搜索关键词" @search="requestBookList(true)" @clear="requestBookList(true)" />
      <van-list v-model:loading="state.loading" :finished="state.finished" finished-text="没有更多数据" :immediate-check="false" @load="requestBookList(false)">
        <book-item v-for="book in books" :key="book.book_id" :book="book" />
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, reactive} from 'vue'
import {getBookList, addMyBook} from "@/http/api";
import {useRoute, useRouter} from "vue-router";
import {BookModel} from "@/models/models";
import NavigationBar from "@/components/NavigationBar.vue";
import BookItem from "@/components/BookItem.vue";

export default defineComponent({
  name: "Books",
  components: {
    BookItem,
    NavigationBar
  },
  setup() {
    const route = useRoute()
    const cate_id = (route.query.cate_id || '')
    const cate_name = ref('')
    const books = ref<BookModel[]>([])
    const search_word = ref('')
    let pageNum = 1
    const state = reactive({
      refreshing: false,
      loading: false,
      finished: false
    })
    const requestBookList = (refresh:boolean) => {
      if (refresh) {
        pageNum = 1
      } else {
        pageNum++
      }
      // @ts-ignore
      getBookList(pageNum, cate_id, search_word.value, refresh, state).then((res:BookModel[]|any)=>{
        if (refresh) {
          books.value = []
        }
        books.value = books.value.concat(res)
        if (books.value.length > 0) {
          const book = books.value[0]
          cate_name.value = book.cate_name as string
        }
      }).catch(err=>{
        if (!refresh) {
          pageNum--
        }
      })
    }
    requestBookList(true)
    return {
      books,
      cate_name,
      search_word,
      state,
      requestBookList
    }
  }
})
</script>

<style lang="less" scoped>

</style>
