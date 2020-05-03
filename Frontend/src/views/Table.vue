<template>
  <div id="content">
    <div class="table">
      <div class="info">
        <mdb-icon icon="info-circle" size="2x" />
        <p class="text">Table1</p>
      </div>
      <div class="card">
        <TablePage :contents="contents" />
      </div>
      <div class="info">
        <mdb-icon icon="info-circle" size="2x" />
        <p class="text">Table2</p>
      </div>
      <div class="card">
        <TablePage :contents="contents" />
      </div>
    </div>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
import TablePage from "@/components/TablePage.vue";

export default {
  name: "Table",
  components: {
    mdbIcon,
    TablePage,
  },
  data() {
    return {
      contents: [
        { col1: "#", col2: "First", col3: "Last", col4: "Handle" },
        { id: 1, First: "Mark", Last: "Otto", Handle: "@mdo" },
        { id: 2, First: "Jacob", Last: "Thornton", Handle: "@fat" },
        { id: 3, First: "Larry", Last: "the Bird", Handle: "@twitter" },
      ],
    };
  },
};
</script>

<style scoped>
/* Content Card */
#content {
  padding: 40px;
}

.info {
  width: 100%;
  margin-bottom: 10px;
  display: flex;
  flex-direction: row;
}

.text {
  color: #252422;
  font-weight: 500;
  font-size: 1.5em;
  margin-left: 10px;
}

.table .card {
  height: 400px;
  width: 100%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;

  padding: 20px;
  box-sizing: border-box;
}
</style>
