import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: {
        getItem: (key) => Cookies.get(key),
        setItem: (key, value) =>
          Cookies.set(key, value, { expires: 3, secure: false }),
        removeItem: (key) => Cookies.remove(key),
      },
    }),
  ],
  state: {
    user: {},
    isAuthenticated: false,
  },
  mutations: {
    setUserData(state, payload) {
      state.user = payload.userData;
      state.isAuthenticated = true;
    },
    resetState(state) {
      state.user = {};
      state.isAuthenticated = false;
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    getUserEmail(state) {
      return state.user.email;
    },
    getUserName(state) {
      return state.user.username;
    },
  },
  actions: {
    login(context, userData) {
      context.commit("setUserData", { userData });
    },
    reset(context) {
      context.commit("resetState");
    },
  },
  modules: {},
});
