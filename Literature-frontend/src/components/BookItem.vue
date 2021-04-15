<template>
  <div class="item-container" style="flex-direction: row;align-items: center;" @click="toChapterList(book.book_id)">
    <img class="lv" src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2022109321,3932035584&fm=26&gp=0.jpg">
    <div class="rv">
      <h2>{{ book.book_name }}</h2>
      <span>作者：{{ book.author_name }}</span>
      <span>章节数：{{ book.chapter_num }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, PropType} from 'vue'
import {BookModel} from "@/models/models";
import {useRouter} from "vue-router";

export default defineComponent({
  name: "BookItem",
  props: {
    book: Object as PropType<BookModel>
  },
  setup() {
    const router = useRouter()
    const toChapterList = (book_id: number) => {
      router.push({path: '/chapter', query: { book_id: book_id }})
    }
    return {
      toChapterList
    }
  }
})
</script>

<style scoped>
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
