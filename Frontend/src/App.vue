<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app",

  components: {},

  data() {
    return {};
  },

  computed: {
    layout() {
      return this.$store.getters.layout;
    },
  },
};
</script>

<style>
html {
  height: 100%;
  overflow: hidden;
  font-size: 16px;
}

body {
  margin: 0;
  padding: 0;
  font-family: "microsoft yahei", "Verdana", "Lato";
}

ul {
  margin: 0;
  padding: 0;
  list-style-type: none;
  margin-block-start: 0;
  margin-block-end: 0;
  padding-inline-start: 0;
}

a {
  -webkit-tap-highlight-color: rgba(255, 0, 0, 0);
  /* remove blud borders when clicking a tag in mobile end*/
  text-decoration: none;
  color: white;
}

em,
div,
p,
h2,
h3,
h4 {
  font-weight: normal;
  font-style: normal;
  margin: 0;
  padding: 0;
}
</style>
