<template>
  <div id="dashboard">
    <nav class="nav-container">
      <NavSidebar />
    </nav>
    <div class="view-container">
      <!-- <Header /> -->
      <router-view />
    </div>
  </div>
</template>

<script>
import NavSidebar from "@/components/NavSidebar";
// import Header from "@/components/Header";

export default {
  name: "app",

  components: {
    NavSidebar,
    // Header,
  },

  data() {
    return {};
  },

  computed: {},
};
</script>

<style scoped>
.nav-container {
  width: 300px;
  position: fixed;
  height: 100vh;
  background: #66615b;
  opacity: 0.8;
}

.view-container {
  padding-left: 300px;
  /* padding-right: 50px; */
  overflow: auto;
  height: 100vh;
  background: #f4f3ef;
}
</style>
