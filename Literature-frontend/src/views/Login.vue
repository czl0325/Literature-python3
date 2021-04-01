<template>
  <van-nav-bar title="登录" left-text="返回" fixed border left-arrow @click-left="onBack" />

  <div style="padding-top: 100px;">
    <van-form @submit="onLogin">
      <van-field v-model="info.nickName" name="用户名" label="用户名" placeholder="请输入用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
      <van-field v-model="info.password" type="password" name="密码" label="密码" placeholder="请输入密码" :rules="[{ required: true, message: '请填写密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
  </div>
</template>

<script lang="ts">
import {defineComponent, reactive} from 'vue'
import {useRouter} from "vue-router";

export default defineComponent({
  name: "Login",
  setup() {
    const router = useRouter()
    const info = reactive({
      nickName: '',
      password: ''
    })
    const onBack = () => {
      router.back()
    }
    const onLogin = () => {

    }
    return {
      info,
      onBack,
      onLogin
    }
  }
})
</script>

<style scoped>

</style>
