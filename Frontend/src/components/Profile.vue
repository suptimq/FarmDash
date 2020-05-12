<template>
  <mdb-col>
    <mdb-row>
      <img
        class="img-fluid z-depth-1 rounded-circle img-avatar"
        src="@/assets/cow-avatar.jpg"
        alt="User avatar"
      />
    </mdb-row>
    <mdb-row
      ><h5 class="font-weight-bold mb-4 text-username">
        {{ username }}
      </h5></mdb-row
    >
    <mdb-row
      ><p class="text-email">{{ email }}</p></mdb-row
    >
  </mdb-col>
</template>

<script>
import { mdbRow, mdbCol } from "mdbvue";
export default {
  name: "Profile",
  components: {
    mdbRow,
    mdbCol,
  },
  props: {
    username: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.img-avatar {
  margin: auto;
  margin-top: 30px;
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
  text-align: left;
  opacity: 0.7;
  font-size: 0.9rem;
}
</style>
