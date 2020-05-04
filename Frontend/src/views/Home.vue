<template>
  <div class="home">
    <section id="content" class="content">
      <div class="stat first-row">
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Fat</p>
        </div>
        <div class="card">
          <BarPlotChart
            class="chart"
            :chart-data="barData"
            :options="barOptions"
          />
        </div>
        <div class="card"></div>
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Protein</p>
        </div>
        <div class="card">
          <PiePlotChart
            class="chart"
            :chart-data="pieData"
            :options="pieOptions"
          />
        </div>
        <div class="card"></div>
      </div>
      <div class="whole second-row">
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Profitability</p>
        </div>
        <div class="card">
          <LinePlotChart :chart-data="barData" :options="barOptions" />
        </div>
      </div>
    </section>

    <footer class="footer"></footer>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
import charts from "@/services/charts.js";
import BarPlotChart from "@/services/charts/BarPlotChart.js";
import PiePlotChart from "@/services/charts/PiePlotChart.js";
import LinePlotChart from "@/services/charts/LinePlotChart.js";

export default {
  name: "Home",
  components: {
    mdbIcon,
    BarPlotChart,
    PiePlotChart,
    LinePlotChart,
  },
  data() {
    return {
      barData: Object,
      barOptions: Object,
      pieData: Object,
      pieOptions: Object,
      lineData: Object,
      lineOptions: Object,
    };
  },
  created() {
    [this.barData, this.barOptions] = charts.fillBarData();
    [this.pieData, this.pieOptions] = charts.fillPieData();
    [this.lineData, this.lineOptions] = charts.fillBarData();
  },
  methods: {},
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

.chart {
  height: 100%;
  width: 80%;
  margin: auto;
}
</style>
