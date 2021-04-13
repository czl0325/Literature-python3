<template>
  <navigation-bar :title="book.book_name" />
  <div class="my-container">
    <van-pull-refresh v-model="state.refreshing" style="width: 100%;min-height: 100vh;" @refresh="requestChapterList(true)">
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
import {useRoute} from "vue-router";
import {getBookDetail, getChapterList} from "@/http/api";
import ChapterItem from "@/components/ChapterItem.vue";

export default defineComponent({
  name: "ChapterList",
  components: {
    ChapterItem,
    NavigationBar
  },
  setup() {
    const route = useRoute()
    //const router = useRouter()
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
      requestChapterList
    }
  }
})
</script>

<style scoped>

</style>
