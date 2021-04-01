<template>
  <navigation-bar title="注册"></navigation-bar>

  <div class="my-container">
    <van-form @submit="onResister">
      <van-field v-model="user.userName" name="用户名" label="用户名" placeholder="请输入用户名" :rules="[{ required: true, message: '请填写用户名' }]"
      />
      <van-field v-model="user.password" type="password" name="密码" label="密码" placeholder="请输入密码" :rules="[{ required: true, message: '请填写密码' }]"
      />
      <van-field name="radio" label="性别">
        <template #input>
          <van-radio-group v-model="user.gender" direction="horizontal">
            <van-radio :name="1">男</van-radio>
            <van-radio :name="0">女</van-radio>
          </van-radio-group>
        </template>
      </van-field>
      <van-field v-model="user.location" readonly clickable name="area" label="地区选择" placeholder="点击选择省市区" @click="state.showArea=true"
      />
      <van-field name="uploader" label="上传头像">
        <template #input>
          <van-uploader v-model="files" :max-count="1"/>
        </template>
      </van-field>
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          点击注册
        </van-button>
      </div>
    </van-form>
  </div>


  <van-popup v-model:show="state.showArea" position="bottom">
    <van-area title="选择省市区" :area-list="areaListRef" @confirm="onConfirmLocation" @cancel="state.showArea=false"/>
  </van-popup>
</template>

<script lang="ts">
import {defineComponent, reactive, ref} from 'vue'
import NavigationBar from "@/components/NavigationBar.vue";
import {areaList} from '@/tools/areas'

export default defineComponent ({
  name: "Register",
  components: {
    NavigationBar
  },
  setup() {
    const user = reactive({
      userName: '',
      password: '',
      gender: 0,
      location: '',
      avatarUrl: ''
    })
    const files = ref([])
    const state = reactive({
      showArea: false
    })
    const areaListRef = ref(areaList)
    const onConfirmLocation = (value: any) => {
      state.showArea = false;
      user.location = value
          .filter((item: any) => !!item)
          .map((item: any) => item.name)
          .join('/');
    }
    const onResister = () => {
      console.log(user)
      console.log(files)
    }
    return {
      user,
      state,
      files,
      areaListRef,
      onConfirmLocation,
      onResister
    }
  }
})
</script>

<style scoped>

</style>
