import {createStore} from "vuex";
import state from "@/store/state";
import mutations from "@/store/mutations";
import VueXAlong from 'vuex-along';

export default createStore({
  state,
  mutations,
  plugins: [VueXAlong({
    name: 'Literature',     //存放在localStroage或者sessionStroage 中的名字
    // @ts-ignore
    local: false,           //是否存放在local中  false 不存放 如果存放按照下面session的配置配
  })]
})
