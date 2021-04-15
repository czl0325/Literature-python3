<template>
  <navigation-bar title="我的书架" />
  <div class="my-container">
    <van-pull-refresh style="width: 100%;min-height: 100vh;" v-model="state.refreshing" @refresh="requestBookList(true)">
      <van-search v-model="search_word" placeholder="请输入搜索关键词" @search="requestBookList(true)" @clear="requestBookList(true)" />
      <book-item v-for="book in books" :key="book.book_id" :book="book" />
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
    const requestBookList = () => {
      getMyBook(store.state.userInfo.id, search_word.value).then((res:BookModel[]|any)=>{
        books.value = res
        state.refreshing = false
      }).catch(err=>state.refreshing = false)
    }
    requestBookList()
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
