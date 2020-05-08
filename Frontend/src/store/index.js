import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    layout: "SignLayout",
    user: {},
    isAuthenticated: true,
  },
  mutations: {
    setUserData(state, payload) {
      state.user = payload.userData;
      state.isAuthenticated = true;
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
  },
  actions: {
    login(context, userData) {
      context.commit("setUserData", { userData });
    },
  },
  modules: {},
});
