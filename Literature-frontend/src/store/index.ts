import {createStore} from "vuex";
import state from "@/store/state";
import mutations from "@/store/mutations";
import VueXAlong from 'vuex-along';

const store = createStore({
  state,
  mutations,
  plugins: [VueXAlong({
    name: 'Literature',
    session: { list: ['userInfo'], isFilter: false }
  })]
})

export default store;
