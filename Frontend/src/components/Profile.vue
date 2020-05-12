<template>
  <mdb-col>
    <mdb-row>
      <img
        class="img-fluid z-depth-1 rounded-circle img-avatar"
        src="@/assets/cow-avatar.jpg"
        alt="User avatar"
      />
    </mdb-row>
    <mdb-row><h5 class="font-weight-bold mb-4 text-profile">Ken</h5></mdb-row>
    <mdb-row><p class="text-profile text-muted">Email</p></mdb-row>
  </mdb-col>
</template>

<script>
import { mdbRow, mdbCol } from "mdbvue";
export default {
  name: "Profile",
  components: {
    mdbRow,
    mdbCol
  }
};
</script>

<style scoped>
.img-avatar {
  margin: auto;
  max-width: 100px;
  max-height: 100px;
}
.text-profile {
  margin: auto;
  text-align: center;
}
</style>