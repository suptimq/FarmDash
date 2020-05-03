<template>
  <div id="tablePage">
    <mdb-tbl striped>
      <mdb-tbl-head>
        <tr>
          <th v-for="(header, key) in contents[0]" :key="key">
            {{ header }}
          </th>
        </tr>
      </mdb-tbl-head>

      <mdb-tbl-body>
        <tr
          v-for="content in contents.slice(1, contents.length)"
          :key="content.id"
        >
          <td v-for="(item, key) in content" :key="key">
            {{ item }}
          </td>
        </tr>
      </mdb-tbl-body>
    </mdb-tbl>
  </div>
</template>

<script>
import { mdbTbl, mdbTblHead, mdbTblBody } from "mdbvue";

export default {
  name: "TablePage",
  components: {
    mdbTbl,
    mdbTblHead,
    mdbTblBody,
  },
  props: {
    contents: Array,
  },
};
</script>
