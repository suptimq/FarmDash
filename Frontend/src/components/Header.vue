<template>
  <div>
    <header class="header">
      <div class="search pos">
        <!-- <p class="text">Overview</p> -->
        <div class="alert alert-dark" role="alert">
          The number of cows: {{ numOfCow }}
        </div>
        <div class="input">
          <Dropdown
            :items="cows"
            :selected="selected"
            :scroll="scroll"
            @fetchItemID="handleFetch"
          ></Dropdown>
        </div>
      </div>
      <div class="status pos">
        <p class="text">
          <mdb-icon icon="chalkboard" />
          Stats
        </p>
        <p class="text">
          <mdb-icon far icon="bell" />
          5
        </p>
        <p class="text">
          <mdb-icon icon="cog" />
          Settings
        </p>
      </div>
    </header>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
// eslint-disable-next-line no-unused-vars
import backend from "@/services/backend.js";
import Dropdown from "@/components/Dropdown.vue";

export default {
  components: {
    mdbIcon,
    Dropdown,
  },
  props: {
    cowData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      cowsId: Array,
      selected: Number,
      scroll: true,
    };
  },
  created() {
    // Sort the ID
    this.cowsId = this.cowData
      .slice(0, this.cowData.length)
      .sort((a, b) => parseInt(a) - parseInt(b));
    // Number -100 means the whole herds
    if (this.cowsId[this.cowsId.length - 1] !== -100) {
      this.cowsId.push(-100);
    }
    this.selected = this.cowsId[this.cowsId.length - 1];
  },
  computed: {
    cows: function() {
      var cows = [];
      for (const id of this.cowsId) {
        var tmp = {};
        tmp["id"] = id;
        if (id === -100) {
          tmp["name"] = "HERDS";
        } else {
          tmp["name"] = "COW " + id;
        }
        cows.push(tmp);
      }

      return cows;
    },
    numOfCow: function() {
      return this.cowsId.length - 1;
    },
  },
  methods: {
    handleFetch(id) {
      this.$router.push({ path: `/home/${id}` });
    },
  },
};
</script>

<style scoped>
/* Header */
header {
  color: #777;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #777;
}

.input {
  margin-left: 10px;
}

.pos {
  margin: 12px 0 0;
  padding: 15px;
}

.search {
  display: flex;
  justify-content: space-between;
}

.search .text {
  font-weight: 600;
  font-size: 20px;
  padding: 10px 15px 0 0;
}

.status {
  display: flex;
  justify-content: space-between;
}

.status .text {
  font-size: 16px;
  line-height: 1.4em;
  padding: 10px 15px 0 0;
}

.active-cyan .fa,
.active-cyan-2 .fa {
  color: #4dd0e1;
}

.dropdown-divider {
  border-top: 2px solid #e9ecef;
}
</style>
