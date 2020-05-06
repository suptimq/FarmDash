<template>
  <div>
    <header class="header">
      <div class="search pos">
        <p class="text">Overview</p>
        <div class="input">
          <mdb-dropdown>
            <mdb-dropdown-toggle slot="toggle">
              {{ displayID }}
            </mdb-dropdown-toggle>
            <mdb-dropdown-menu>
              <mdb-dropdown-item
                v-for="(cow, idx) in cows"
                :key="cow.id"
                :class="{ active: selected === cow.id }"
              >
                <router-link to="">
                  <span :id="cow.id" @click="getIndividulInfo(cow.id)">
                    {{ cow.name }}
                  </span>
                </router-link>

                <div
                  v-if="idx === cows.length - 2"
                  class="dropdown-divider"
                ></div>
              </mdb-dropdown-item>
            </mdb-dropdown-menu>
          </mdb-dropdown>
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
import {
  mdbIcon,
  mdbDropdown,
  mdbDropdownItem,
  mdbDropdownMenu,
  mdbDropdownToggle,
} from "mdbvue";
// eslint-disable-next-line no-unused-vars
import backend from "@/services/backend.js";

export default {
  components: {
    mdbIcon,
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle,
  },
  data() {
    return {
      cows: [
        { id: 1, name: "COW 1" },
        { id: 2, name: "COW 2" },
        { id: 3, name: "COW 3" },
        { id: 1000, name: "HERDS" },
      ],
      selected: 1000,
    };
  },
  computed: {
    displayID: function() {
      return this.selected === this.cows[this.cows.length - 1].id
        ? "HERDS"
        : "COW ID: " + this.selected;
    },
  },
  methods: {
    async getIndividulInfo(id) {
      var path = "http://localhost:5000/cow";
      const params = { ID: id };
      var fatChartData;
      var proteinChartData;
      try {
        const resp = await backend.fetchResource(path, params);
        console.log(resp);
        console.log(resp["fat_chart_data"]);
        fatChartData = resp["fat_chart_data"];
        proteinChartData = resp["protein_chart_data"];
        this.selected = id;

        this.$router.push({
          path: `/home/${id}`,
          params: { fatData: fatChartData, proteinData: proteinChartData },
        });
      } catch (error) {
        console.log(error);
      }
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

.dropdown-item.active {
  background: lightgray;
}

a {
  color: black;
}

.dropdown-divider {
  border-top: 2px solid #e9ecef;
}
</style>
