<template>
  <div class="top-view">
    <div class="avatar" @click="onLogin"></div>
    <div class="tr">
      <span>{{ user.id ? user.nickName : '未登录' }}</span>
      <span>id: {{ user.id }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import {useStore} from "vuex";
import {GlobalDataProps} from '@/store/state'
import {useRouter} from "vue-router";

export default defineComponent({
  name: "Me",
  setup() {
    const store = useStore<GlobalDataProps>()
    const router = useRouter()
    const user = store.state.userInfo
    const onLogin = () => {
      if (!user.id) {
        router.push('login')
      }
    }
    return {
      user,
      onLogin
    }
  }
})
</script>

<style lang="less" scoped>
@import "../css/common.less";
.top-view {
  background-color: @mainColor;
  width: 100%;
  height: 250px;
  display: flex;
  align-items: center;
  padding: 0 10px;
  box-sizing: border-box;

  .avatar {
    .avatar()

  }

  .tr {
    height: 60px;
    margin-left: 10px;
    .flex-column(space-between);

    span {
      .font-size-color(20px, white);
      &:nth-child(1) {
        font-weight: bold;
      }
    }
  }
}
</style>
