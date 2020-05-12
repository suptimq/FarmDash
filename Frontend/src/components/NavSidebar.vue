<template>
  <div class="side-nav">
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

    <div>
      <mdb-col>
        <mdb-row style="text-align: center">
          <img
            class="img-fluid rounded-circle img-avatar"
            src="@/assets/cow-avatar.jpg"
            alt="User avatar"
          />
        </mdb-row>
        <mdb-row
          ><h4 class="font-weight-bold mb-4 text-username">{{username}}</h4></mdb-row
        >
        <mdb-row><p class="text-email">{{email}}</p></mdb-row>
      </mdb-col>
    </div>

    <div class="logout" @click="logout">
      <mdb-icon icon="sign-out-alt" />
      Logout
    </div>

    <div class="logo">
      <!-- <img src="../assets/dairy-logo.png" /> -->
      <p>
        © Copyright 2020. All Rights Reserved
      </p>
    </div>
  </div>
</template>

<script>
import { mdbIcon, mdbRow, mdbCol } from "mdbvue";

export default {
  components: {
    mdbIcon,
    mdbRow,
    mdbCol,
  },
  data() {
    return {
      username: "Sirui_Wang",
      email: "w305475116@gmail.com",
      selected: "nav1",
      items: [
        {
          id: "nav1",
          name: "DASHBOARD",
          to: "/home/1000",
          icon: "chalkboard"
          // hasSubItem: true,
          // subItems: [{ id: "subnav1", name: "PLACEHOLDER" }],
        }
        // { id: "nav2", name: "USER PROFILE", to: "/user", icon: "user" },
        // { id: "nav3", name: "TABLE LIST", to: "/table", icon: "table" },
      ]
    };
  },
  methods: {
    toggleMenu(id) {
      this.selected = id;
    },
    logout() {
      this.$store.dispatch("reset");
      this.$router.push({ name: "Signin" });
    }
  }
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
  color: #ED9C23;
  font-size: 1.4rem;
}

.logout {
  margin: auto;
  text-align: center;
  cursor: pointer;
}

.img-avatar {
  margin: auto;
  margin-top: -19px;
  max-width: 120px;
  max-height: 120px;
}
.text-username {
  margin: auto;
  margin-top: 15px;
  margin-bottom: -20px;
  text-align: left;
}
.text-email {
  margin: auto;
  margin-top: -20px;
  margin-bottom: 55px;
  text-align: left;
  opacity: 0.7;
  font-size: 0.9rem;
}
</style>