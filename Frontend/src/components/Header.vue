<template>
  <div>
    <header class="header">
      <div class="search">
        <p class="text">Overview</p>
        <div class="input">
          <mdb-form-inline class="active-cyan-2 ">
            <input
              class="form-control mr-sm-2"
              type="text"
              placeholder="Search"
              aria-label="Search"
            />
            <mdbIcon icon="search" />
          </mdb-form-inline>
        </div>
      </div>
      <div class="status">
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
import { mdbIcon, mdbFormInline } from "mdbvue";

export default {
  components: {
    mdbIcon,
    mdbFormInline,
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

.search {
  display: flex;
  justify-content: space-between;
  margin: 12px 0 0;
  padding: 15px;
}

.search .text {
  font-weight: 600;
  font-size: 20px;
  padding: 10px 15px 0 0;
}

.status {
  display: flex;
  justify-content: space-between;
  margin: 12px 0 0;
  padding: 15px;
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
</style>
