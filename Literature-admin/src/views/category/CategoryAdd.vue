<template>
  <el-form ref="form" :model="category" :rules="rules" label-width="100px">
    <el-form-item label="分类名称" prop="cate_name">
      <el-input v-model="category.cate_name" />
    </el-form-item>
    <el-form-item label="分类图片">
      <el-upload class="avatar-uploader" :show-file-list="false" action="">
        <img v-if="category.cate_icon" :src="category.cate_icon" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {CategoryModel} from "@/models/category";

export default defineComponent ({
  name: "CategoryAdd",
  setup() {
    const category = ref<CategoryModel|any>({})
    const rules = {
      cate_name: [
        {required: true, message: '请输入分类名称', trigger: 'blur'},
      ]
    }
    return {
      category,
      rules
    }
  }
})
</script>

<style lang="less" scoped>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;

  &:hover {
    border-color: #409EFF;
  }
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
