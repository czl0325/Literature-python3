<template>
  <navigation-bar :title="chapter.chapter_name"/>
  <div class="my-container">
    <p class="title">{{ chapter.chapter_name }}</p>
    <div class="content">{{ chapter.content }}</div>
  </div>
  <div class="bottom-view">
    <van-button type="primary" size="large" @click="toChapter(false)">上一章</van-button>
    <van-button type="primary" size="large" @click="toChapter(true)">下一章</van-button>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, watch} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";
import {ChapterModel} from "@/models/models";
import {getChapterDetail1, getChapterDetail2} from '@/http/api'
import {useRoute, useRouter} from 'vue-router'

export default defineComponent({
  name: "ChapterContent",
  components: {NavigationBar},
  setup() {
    const chapter = ref<ChapterModel>({})
    const route = useRoute()
    const router = useRouter()
    const id = (route.query.id || '0')
    const chapter_id = (route.query.chapter_id || '0')
    const book_id = (route.query.book_id || '0')
    if (parseInt(id as string) > 0) {
      getChapterDetail1(parseInt(id as string)).then((res:ChapterModel|any)=>{
        chapter.value = res
        window.scrollTo(0, 0)
      })
    } else if (parseInt(chapter_id as string) > 0) {
      getChapterDetail2(parseInt(chapter_id as string), parseInt(book_id as string)).then((res:ChapterModel|any)=>{
        chapter.value = res
        window.scrollTo(0, 0)
      })
    }
    const toChapter = (next: boolean) => {
      const chapter_num = chapter.value.chapter_id
      if (chapter_num) {
        router.push({path: '/content', query: {chapter_id: next?chapter_num+1:chapter_num-1, book_id: chapter.value.book_id}, replace: true})
        // getChapterDetail2(next?chapter_num+1:chapter_num-1, chapter.value.book_id as number).then((res:ChapterModel|any)=>{
        //   chapter.value = res;
        //   window.scrollTo(0, 0)
        // })
      }
    }
    watch(()=>[route.query.chapter_id, route.query.book_id], (val) => {
      if (route.name === 'content') {
        getChapterDetail2(parseInt(route.query.chapter_id as string), parseInt(route.query.book_id as string)).then((res:ChapterModel|any)=>{
          chapter.value = res
          window.scrollTo(0, 0)
        })
      }
    })
    return {
      chapter,
      toChapter
    }
  }
})
</script>

<style lang="less" scoped>
.title {
  font-size: 28px;
  font-weight: bold;
  margin: 10px auto;
}
.content {
  padding: 10px 5px 50px;
  box-sizing: border-box;
  white-space: pre-wrap;
  font-size: 18px;
}
.bottom-view {
  margin: 10px auto 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  bottom: 0;
  left: 0;
  height: 50px;
}
</style>
