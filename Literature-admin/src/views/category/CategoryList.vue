<template>
  <div>
    <el-table :data="category_list" border style="width: 100%">
      <el-table-column prop="cate_id" label="id" width="120" />
      <el-table-column prop="cate_name" label="分类名称" />
      <el-table-column prop="cate_icon" label="封面" width="200" >
        <template #default="scope">
          <img :src="`http://127.0.0.1:5000/${scope.row.cate_icon}`" style="width: 60px;height: 60px;">
        </template>
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template #default="scope">
          <el-button @click="handleClick(scope.row)" type="danger" round>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {CategoryModel} from "@/models/category";
import {getCategoryList} from "@/http/api";

export default defineComponent({
  name: "CategoryList",
  setup() {
    const category_list = ref<CategoryModel[]>([])
    const handleClick = (cate: CategoryModel) => {
      console.log(cate)
    }
    getCategoryList().then((res:CategoryModel[]|any)=>{
      category_list.value = res
    })
    return {
      category_list,
      handleClick
    }
  }
})
</script>

<style scoped>

</style>
