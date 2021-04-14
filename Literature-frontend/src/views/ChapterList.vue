<template>
  <navigation-bar :title="book.book_name" />
  <div class="my-container">
    <van-pull-refresh v-model="state.refreshing" style="width: 100%;min-height: 100vh;" @refresh="requestChapterList(true)">
      <h3 style="margin: 10px;">简介:</h3>
      <div v-html="book.intro" style="margin: 10px;"></div>
      <span style="margin: 10px;">作者：{{ book.author_name }}</span>
      <div style="text-align: right;">
        <van-button type="primary" size="small" style="width: 80px;margin: 10px;" @click.stop="addBookShelf(book.book_id)">加入书架</van-button>
      </div>
      <van-list v-model:loading="state.loading" :finished="state.finished" finished-text="没有更多数据" :immediate-check="false" @load="requestChapterList(false)">
        <chapter-item v-for="chapter in chapter_list" :key="chapter.chapter_id" :chapter="chapter" />
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<script lang="ts">
import {defineComponent, reactive, ref} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";
import {BookModel, ChapterModel} from "@/models/models";
import {useRoute, useRouter} from "vue-router";
import {addMyBook, getBookDetail, getChapterList} from "@/http/api";
import ChapterItem from "@/components/ChapterItem.vue";
import {useStore} from "vuex";
import {Toast} from "vant";

export default defineComponent({
  name: "ChapterList",
  components: {
    ChapterItem,
    NavigationBar
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const book = ref<BookModel>({})
    const chapter_list = ref<ChapterModel[]>([])
    const book_id = route.query.book_id
    const state = reactive({
      refreshing: false,
      loading: false,
      finished: false
    })
    let pageNum = 1
    const requestChapterList = (refresh: boolean) => {
      if (typeof book_id === 'string') {
        if (refresh) {
          pageNum = 1
        } else {
          pageNum++
        }
        getChapterList(parseInt(book_id), pageNum, refresh, state).then((res:ChapterModel[] | any) => {
          if (refresh) {
            chapter_list.value = []
          }
          chapter_list.value = chapter_list.value.concat(res)
        })
      }
    }
    const store = useStore()
    const addBookShelf = (book_id: number) => {
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
    if (typeof book_id === 'string') {
      getBookDetail(parseInt(book_id)).then((res:BookModel|any) => {
        book.value = res
      })
      requestChapterList(true)
    }
    return {
      book,
      chapter_list,
      state,
      requestChapterList,
      addBookShelf
    }
  }
})
</script>

<style scoped>

</style>
