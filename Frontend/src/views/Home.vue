<template>
  <div class="home">
    <section id="content" class="content">
      <div class="stat first-row">
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Fat</p>
        </div>
        <div class="card"></div>
        <div class="card"></div>
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Protein</p>
        </div>
        <div class="card"></div>
        <div class="card"></div>
      </div>
      <div class="whole second-row">
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Profitability</p>
        </div>
        <div class="card"></div>
      </div>
    </section>

    <footer class="footer"></footer>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";

export default {
  name: "Home",
  components: {
    mdbIcon,
  },
};
</script>

<style scoped>
/* Content Card */
#content {
  padding: 40px;
}

.stat {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
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

.stat .card {
  height: 300px;
  width: 48%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;
}

.whole .card {
  height: 400px;
  width: 100%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;
}
</style>
