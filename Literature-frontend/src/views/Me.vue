<template>
  <div class="top-view">
    <div class="avatar">

    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Me",
  setup() {

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


}
</style>
