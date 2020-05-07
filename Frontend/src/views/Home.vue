<template>
  <div class="home">
    <div class="d-flex justify-content-center" v-if="loading">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else id="content" class="content">
      <div class="stat first-row">
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Fat</p>
          <Dropdown
            class="date dropdown"
            :items="monthList"
            :selected="fatSelectedMonth"
            @fetchItemID="handleFatMonth"
          ></Dropdown>
          <Dropdown
            class="date dropdown"
            :items="yearList"
            :selected="fatSelectedYear"
            @fetchItemID="handleFatYear"
          ></Dropdown>
          <!-- <p>{{ fatChartData }}</p> -->
        </div>
        <div class="card">
          <BarPlotChart
            class="chart"
            :chart-data="fatChartData"
            :options="chartOptions"
          />
        </div>
        <div class="card"></div>
        <div class="info">
          <mdb-icon icon="info-circle" size="2x" />
          <p class="text">Average Protein</p>
          <Dropdown
            class="date dropdown"
            :items="monthList"
            :selected="proteinSelectedMonth"
            @fetchItemID="handleProteinMonth"
          ></Dropdown>
          <Dropdown
            class="date dropdown"
            :items="yearList"
            :selected="proteinSelectedYear"
            @fetchItemID="handleProteinYear"
          ></Dropdown>
        </div>
        <div class="card">
          <!-- <PiePlotChart
            class="chart"
            :chart-data="pieData"
            :options="pieOptions"
          /> -->
          <BarPlotChart
            class="chart"
            :chart-data="proteinChartData"
            :options="chartOptions"
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
    </div>

    <footer class="footer"></footer>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
import charts from "@/services/charts.js";
import BarPlotChart from "@/services/charts/BarPlotChart.js";
// import PiePlotChart from "@/services/charts/PiePlotChart.js";
import LinePlotChart from "@/services/charts/LinePlotChart.js";
import backend from "@/services/backend.js";
import Dropdown from "@/components/Dropdown.vue";

export default {
  name: "Home",
  props: {
    // Dictionary: key-month, value-records within that month
  },
  components: {
    mdbIcon,
    BarPlotChart,
    LinePlotChart,
    Dropdown,
  },
  data() {
    return {
      loading: true,
      // These two variables store all the data
      fat: Object,
      protein: Object,
      //
      fatData: Object,
      proteinData: Object,
      barData: Object,
      barOptions: Object,
      pieData: Object,
      pieOptions: Object,
      lineData: Object,
      lineOptions: Object,
      fatSelectedMonth: 1,
      fatSelectedYear: 2018,
      proteinSelectedMonth: 1,
      proteinSelectedYear: 2018,
      monthList: [
        { id: 1, name: "Jan" },
        { id: 2, name: "Feb" },
        { id: 3, name: "Mar" },
        { id: 4, name: "April" },
        { id: 5, name: "May" },
        { id: 6, name: "June" },
        { id: 7, name: "July" },
        { id: 8, name: "Aug" },
        { id: 9, name: "Sept" },
        { id: 10, name: "Oct" },
        { id: 11, name: "Nov" },
        { id: 12, name: "Dec" },
      ],
      yearList: [
        { id: 2018, name: "2018" },
        { id: 2019, name: "2019" },
      ],
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    };
  },
  created() {
    [this.barData, this.barOptions] = charts.fillBarData();
    [this.pieData, this.pieOptions] = charts.fillPieData();
    [this.lineData, this.lineOptions] = charts.fillBarData();
    // Data from backend
    this.getHerdsData(this.$route.params.id);
  },
  mounted() {},
  updated() {},
  computed: {
    fatChartData: function() {
      console.log("computed");
      // console.log(this.fatData);
      const [key, val] = Object.entries(this.fatData)[
        this.fatSelectedMonth - 1
      ];

      return this.fillBarData(key, val);
    },
    proteinChartData: function() {
      const [key, val] = Object.entries(this.proteinData)[
        this.proteinSelectedMonth - 1
      ];

      return this.fillBarData(key, val);
    },
  },
  watch: {
    // React to params changes will not call the lifecycle hooks
    $route(to) {
      this.getHerdsData(to.params.id);
    },
    // Watch fatSelectedYear and proteinSelectedYear
    fatSelectedYear: function(year) {
      console.log("watch");
      this.fatData = this.fat[year];
    },
    proteinSelectedYear: function(year) {
      this.proteinData = this.protein[year];
    },
  },
  methods: {
    async getHerdsData(id) {
      // var path = "http://localhost:5000/cow";
      var path =
        "http://flask-env-usingpython36.eba-zhya6xfu.us-east-1.elasticbeanstalk.com/cow";
      id = 26;
      const params = { ID: id };
      try {
        const resp = await backend.fetchResource(path, params);
        // console.log(resp);
        // console.log(resp["fat_chart_data"]);
        this.fat = resp["fat_chart_data"];
        this.protein = resp["protein_chart_data"];
        this.fatData = this.fat[this.fatSelectedYear];
        this.proteinData = this.protein[this.proteinSelectedYear];
        // Set loading status
        this.loading = false;
      } catch (error) {
        console.log(error);
      }
    },
    fillBarData(key, val) {
      var chartData = {};
      var datasets = [];
      var numOfDay = val.length;
      var labels = this.range(1, numOfDay);

      var tmpList = {};
      tmpList["label"] = key;
      tmpList["backgroundColor"] = "#f87979";
      tmpList["data"] = val;

      datasets.push(tmpList);

      chartData["labels"] = labels;
      chartData["datasets"] = datasets;

      return chartData;
    },
    // Likewise Python range() function
    range(low, high) {
      var list = [];
      for (let i = low; i <= high; i++) {
        list.push(i);
      }
      return list;
    },
    handleFatMonth(id) {
      this.fatSelectedMonth = id;
    },
    handleProteinMonth(id) {
      this.proteinSelectedMonth = id;
    },
    handleFatYear(id) {
      this.fatSelectedYear = id;
    },
    handleProteinYear(id) {
      this.proteinSelectedYear = id;
    },
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

.chart {
  height: 100%;
  width: 80%;
  margin: auto;
}

.date.dropdown {
  margin-left: 15px;
  margin-top: -5px;
}

.spinner-border {
  margin-top: 30%;
}
</style>
