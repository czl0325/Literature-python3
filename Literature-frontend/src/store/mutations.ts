import {UserInfo} from "@/store/state";
import {MutationTree} from 'vuex'

const mutations: MutationTree<any> = {
  updateUserInfo(state, user: UserInfo) {
    state.userInfo = user
  }
}

export default mutations;
