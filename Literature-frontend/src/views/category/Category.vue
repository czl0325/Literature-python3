<template>
  <van-nav-bar title="分类" fixed/>
  <div class="my-container">
    <van-grid clickable :column-num="2" style="width: 100%; padding: 10px; box-sizing: border-box" :gutter="10">
      <van-grid-item v-for="cate in categories" :key="cate.cate_id" :icon="cate.cate_icon" :text="cate.cate_name" :to="{path: '/books', query: {cate_id: cate.cate_id}}" direction="horizontal" />
    </van-grid>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {CategoryModel} from "@/models/models";
import {getCategoryList} from "@/http/api";

export default defineComponent ({
  name: "Category",
  setup() {
    const categories = ref<CategoryModel[]>([])
    getCategoryList().then((res:CategoryModel[]|any)=>{
      categories.value = res
    })
    return {
      categories
    }
  }
})
</script>

<style scoped>

</style>
