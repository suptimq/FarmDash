import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Table from "@/views/Table.vue";
import SignIn from "@/components/SignIn.vue";
import SignUp from "@/components/SignUp.vue";
import Forget from "@/components/Forget.vue";
import Reset from "@/components/Reset.vue";
import Profile from "@/components/Profile.vue";

import Dash from "@/views/Dash.vue";
import PageNotFound from "@/views/PageNotFound.vue";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: {
      name: "Signin",
    },
  },
  {
    path: "/signin",
    name: "Signin",
    component: SignIn,
  },
  {
    path: "/test",
    name: "Test",
    component: Profile,
  },
  {
    path: "/forgetpassword",
    name: "Forget",
    component: Forget,
  },
  {
    path: "/resetpassword",
    name: "Reset",
    component: Reset,
  },
  {
    path: "/signup",
    name: "Signyp",
    component: SignUp,
  },
  {
    path: "*",
    component: PageNotFound,
  },
  {
    path: "/",
    name: "Dashboard",
    component: Dash,
    children: [
      {
        path: "/home/:id",
        name: "HomeId",
        component: Home,
        props: true,
        beforeEnter(to, from, next) {
          if (!store.getters.isAuthenticated) {
            next("/signin");
          } else {
            next();
          }
        },
      },
      {
        path: "/user",
        name: "User",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "about" */ "../views/User.vue"),
      },
      {
        path: "/table",
        name: "Table",
        component: Table,
      },
    ],
  },
];

const router = new VueRouter({
  routes,
});

export default router;
