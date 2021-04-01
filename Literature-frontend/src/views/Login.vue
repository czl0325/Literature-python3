<template>
  <navigation-bar title="登录"></navigation-bar>

  <div class="my-container">
    <van-form @submit="onLogin" style="margin-top: 20px;">
      <van-field v-model="info.nickName" name="用户名" label="用户名" placeholder="请输入用户名" :rules="[{ required: true, message: '请填写用户名' }]" />
      <van-field v-model="info.password" type="password" name="密码" label="密码" placeholder="请输入密码" :rules="[{ required: true, message: '请填写密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="primary" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
    <span class="register" @click="toRegister">没有账号？点击注册。</span>
  </div>
</template>

<script lang="ts">
import {defineComponent, reactive} from 'vue'
import {useRouter} from "vue-router";
import NavigationBar from "@/components/NavigationBar.vue";

export default defineComponent({
  name: "Login",
  components: {
    NavigationBar
  },
  setup() {
    const router = useRouter()
    const info = reactive({
      nickName: '',
      password: ''
    })
    const onLogin = () => {

    }
    const toRegister = () => {
      router.push('register')
    }
    return {
      info,
      onLogin,
      toRegister
    }
  }
})
</script>

<style lang="less" scoped>
.register {
  margin: 10px auto 0;
  color: indianred;
  font-size: 14px;
}
</style>
