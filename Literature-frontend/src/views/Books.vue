<template>
  <navigation-bar :title="cate_name"/>
  <div class="my-container">
    <van-pull-refresh style="width: 100%;min-height: 100vh;" v-model="state.refreshing" @refresh="requestBookList(true)">
      <van-list v-model:loading="state.loading" :finished="state.finished" finished-text="没有更多数据" :immediate-check="false" @load="requestBookList(false)">
        <div v-for="book in books" :key="book.book_id" class="item-container" style="flex-direction: row;align-items: center;" @click="toChapterList(book.book_id)">
          <img class="lv" src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2022109321,3932035584&fm=26&gp=0.jpg">
          <div class="rv">
            <h2>{{ book.book_name }}</h2>
            <span>作者：{{ book.author_name }}</span>
            <span>章节数：{{ book.chapter_num }}</span>
          </div>
          <van-button type="primary" size="large" style="width :100px;height: 40px;" @click.stop="addBookShelf(book.book_id)">加入书架</van-button>
        </div>
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
import {useStore} from "vuex";
import {Toast} from "vant";

export default defineComponent({
  name: "Books",
  components: {
    NavigationBar
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const cate_id = (route.query.cate_id || '')
    const cate_name = ref('')
    const books = ref<BookModel[]>([])
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
      getBookList(pageNum, cate_id, refresh, state).then((res:BookModel[]|any)=>{
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
    const toChapterList = (book_id: number) => {
      console.log("书籍id=", book_id)
      router.push({path: '/chapter', query: { book_id: book_id }})
    }
    const store = useStore()
    const addBookShelf = (book_id: number) => {
      console.log("书籍id=", book_id)
      if (!store.state.userInfo.id) {
        Toast.fail('请先登录')
        router.push('login')
        return
      }
      Toast.loading('正在添加书籍到书架...')
      addMyBook(book_id, store.state.userInfo.id).then(()=>{
        Toast.success('添加成功!')
      })
    }
    requestBookList(true)
    return {
      books,
      cate_name,
      toChapterList,
      state,
      requestBookList,
      addBookShelf
    }
  }
})
</script>

<style lang="less" scoped>
.lv {
  width: 80px;
  height: 120px;
  object-fit: contain;
}
.rv {
  height: 120px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  margin-left: 15px;
}
</style>
