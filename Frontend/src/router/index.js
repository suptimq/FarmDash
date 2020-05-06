import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Table from "@/views/Table.vue";
import SignIn from "@/components/SignIn.vue";
import Dash from "@/views/Dash.vue";

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
    path: "/",
    name: "Dashboard",
    component: Dash,
    children: [
      {
        path: "/home",
        name: "Home",
        component: Home,
      },
      {
        path: "/home/:id",
        name: "HomeId",
        component: Home,
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
