<template>
  <div class="side-nav">
    <Profile :username="username" :email="email"></Profile>

    <ul class="nav-items">
      <li class="nav-item" v-for="item in items" :key="item.id">
        <mdb-icon :icon="item.icon" />
        <router-link
          :to="item.to"
          class="nav-link main-item"
          :class="{ active: selected === item.id }"
        >
          <span :id="item.id" @click="toggleMenu(item.id)">
            {{ item.name }}
          </span>
        </router-link>
        <ul v-if="item.hasSubItem" class="sub-nav-items">
          <li v-for="subItem in item.subItems" :key="subItem.id">
            {{ subItem.name }}
          </li>
        </ul>
      </li>
    </ul>

    <div class="logout" @click="logout">
      <mdb-icon icon="sign-out-alt" />
      Logout
    </div>

    <div class="logo">
      <p>
        © Copyright 2020. All Rights Reserved
      </p>
    </div>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
import Profile from "@/components/Profile.vue";
import store from "@/store";

export default {
  components: {
    mdbIcon,
    Profile,
  },
  data() {
    return {
      username: "",
      email: "",
      selected: "nav1",
      items: [
        {
          id: "nav1",
          name: "DASHBOARD",
          to: "/home/1000",
          icon: "chalkboard",
        },
      ],
    };
  },
  created() {
    this.email = store.getters.getUserEmail;
    this.username = store.getters.getUserName;
  },
  methods: {
    toggleMenu(id) {
      this.selected = id;
    },
    logout() {
      this.$store.dispatch("reset");
      this.$router.push({ name: "Signin" });
    },
  },
};
</script>

<style scoped>
.nav-items {
  margin: 3em 2em 1em 3em;
}

.sub-nav-items {
  margin-left: 2em;
  margin-bottom: 0.8em;
}
.sub-nav-items li {
  font-size: 18px;
  line-height: 24px;
  margin-bottom: 0.6em;
}

.nav-link {
  color: white;
  text-decoration: none;
  display: inline-block;
}

.main-item {
  font-size: 20px;
  margin: 0 0 0.8em 0;
}

.logo {
  bottom: 10px;
  position: absolute;
  text-align: center;
  width: 100%;
}

img {
  width: 50%;
}
img p {
  font-size: 10px;
}

.side-nav {
  color: white;
  opacity: 0.9;
}

.nav-link.active {
  /*color: #41b883;*/
  color: #ed9c23;
  font-size: 1.4rem;
}

.logout {
  margin: auto;
  text-align: center;
  cursor: pointer;
}
</style>
