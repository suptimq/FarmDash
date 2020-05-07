<template>
  <div>
    <mdb-dropdown>
      <mdb-dropdown-toggle slot="toggle">
        {{ displayID }}
      </mdb-dropdown-toggle>
      <mdb-dropdown-menu>
        <mdb-dropdown-item
          v-for="(item, idx) in items"
          :key="idx"
          :class="{ active: selectedTag === item.id }"
        >
          <router-link to="">
            <span :id="item.id" @click="getID(item.id)">
              {{ item.name }}
            </span>
          </router-link>
        </mdb-dropdown-item>
      </mdb-dropdown-menu>
    </mdb-dropdown>
  </div>
</template>

<script>
import {
  mdbDropdown,
  mdbDropdownItem,
  mdbDropdownMenu,
  mdbDropdownToggle,
} from "mdbvue";

export default {
  components: {
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle,
  },
  props: {
    items: {
      type: Array,
      required: true,
    },
    selected: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      selectedTag: "",
    };
  },
  created() {
    this.selectedTag = this.selected;
  },
  methods: {
    getID(id) {
      this.selectedTag = id;
      this.$emit("fetchItemID", id);
    },
  },
  computed: {
    displayID: function() {
      for (const item of this.items) {
        if (item.id === this.selectedTag) {
          return item.name;
        }
      }

      return "NOT FOUND";
    },
  },
};
</script>

<style scoped>
.dropdown-item.active {
  background: lightgray;
}
a {
  color: black;
}
</style>
