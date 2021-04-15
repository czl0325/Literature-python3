<template>
  <navigation-bar title="我的书架" />
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
import {defineComponent, reactive, ref} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";
import {getMyBook} from "@/http/api";
import {useStore} from "vuex";
import BookItem from "@/components/BookItem.vue";
import {BookModel} from "@/models/models";

export default defineComponent({
  name: "MyBooks",
  components: {BookItem, NavigationBar},
  setup() {
    const state = reactive({
      refreshing: false,
      loading: false,
      finished: false
    })
    const search_word = ref('')
    const store = useStore()
    const books = ref<BookModel[]>([])
    let pageNum = 1
    const requestBookList = (refresh: boolean) => {
      if (refresh) {
        pageNum = 1
      } else {
        pageNum++
      }
      getMyBook(store.state.userInfo.id, search_word.value, pageNum, refresh, state).then((res:BookModel[]|any)=>{
        if (refresh) {
          books.value = []
        }
        books.value = books.value.concat(res)
      })
    }
    requestBookList(true)
    return {
      state,
      search_word,
      books,
      requestBookList
    }
  }
})
</script>

<style scoped>

</style>
