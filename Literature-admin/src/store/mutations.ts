import {MutationTree} from "vuex";

export const mutations: MutationTree<any> = {
  updateTabs(state, payload) {
    state.tabs = payload
  }
}
