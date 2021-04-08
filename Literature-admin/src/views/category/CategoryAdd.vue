<template>
  <el-form ref="form" :model="category" :rules="rules" label-width="100px">
    <el-form-item label="分类名称" prop="cate_name">
      <el-input v-model="category.cate_name" />
    </el-form-item>
    <el-form-item label="分类图片" >
      <el-upload action="#" :before-upload="beforeImageUpload">
        <el-button size="small" type="primary">选择图片</el-button>
        <span style="display: inline; margin-left: 10px;">{{ uploadFile.name }}</span>
      </el-upload>
    </el-form-item>
    <el-form-item>
      <el-button style="margin-top: 30px;" type="primary" @click="onAddCategory">立即添加分类</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {CategoryModel} from "@/models/models";
import {FileModel} from "@/http/myAxios";
import {addCategory} from "@/http/api";
import {ElMessage} from "element-plus";

export default defineComponent ({
  name: "CategoryAdd",
  setup() {
    const category = ref<CategoryModel|any>({})
    const rules = {
      cate_name: [
        {required: true, message: '请输入分类名称', trigger: 'blur'},
      ]
    }
    const uploadFile = ref<FileModel|any>({})
    const beforeImageUpload = (file: FileModel) => {
      uploadFile.value = file
    }
    const onAddCategory = () => {
      addCategory(uploadFile.value, category.value.cate_name).then(res=>{
        ElMessage.success('添加成功')
      })
    }
    return {
      category,
      rules,
      uploadFile,
      beforeImageUpload,
      onAddCategory
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
  background-color: #8c939d;
  color: white;
  width: 80px;
  height: 80px;
  line-height: 80px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
