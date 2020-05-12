<template>
  <div class="home">
    <div class="d-flex justify-content-center" v-if="loading">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else>
      <Header :cowData="cows" />
      <div id="content" class="content">
        <div class="stat first-row">
          <!-- Fat -->
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
          </div>
          <div class="card">
            <BarPlotChart
              class="chart"
              :chart-data="fatBarData"
              :options="avgBarChartOptions"
            />
          </div>
          <!-- Protein -->
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
            <BarPlotChart
              class="chart"
              :chart-data="proteinBarData"
              :options="avgBarChartOptions"
            />
          </div>
          <!-- Yield -->
          <div class="info">
            <mdb-icon icon="info-circle" size="2x" />
            <p class="text">Yield</p>
            <Dropdown
              class="date dropdown"
              :items="monthList"
              :selected="yieldSelectedMonth"
              @fetchItemID="handleYieldMonth"
            ></Dropdown>
            <Dropdown
              class="date dropdown"
              :items="yearList"
              :selected="yieldSelectedYear"
              @fetchItemID="handleYieldYear"
            ></Dropdown>
          </div>
          <div class="card yield">
            <BarPlotChart
              class="chart"
              :chart-data="yieldBarData"
              :options="yieldBarOptions"
            />
          </div>
          <div class="card yield">
            <PiePlotChart
              class="chart"
              :chart-data="yieldPieData"
              :options="pieChartOptions"
            />
          </div>
        </div>
        <div class="whole second-row">
          <div class="info">
            <mdb-icon icon="info-circle" size="2x" />
            <p class="text">Profitability</p>
            <Dropdown
              class="date dropdown"
              :items="monthList"
              :selected="profitSelectedMonth"
              @fetchItemID="handleProfitMonth"
            ></Dropdown>
            <Dropdown
              class="date dropdown"
              :items="yearList"
              :selected="profitSelectedYear"
              @fetchItemID="handleProfitYear"
            ></Dropdown>
          </div>
          <div class="card">
            <LinePlotChart
              :chart-data="profitLineData"
              :options="profitBarOptions"
            />
          </div>
        </div>
      </div>
    </div>

    <footer class="footer"></footer>
  </div>
</template>

<script>
import { mdbIcon } from "mdbvue";
import BarPlotChart from "@/services/charts/BarPlotChart.js";
import PiePlotChart from "@/services/charts/PiePlotChart.js";
import LinePlotChart from "@/services/charts/LinePlotChart.js";
import backend from "@/services/backend.js";
import Dropdown from "@/components/Dropdown.vue";
import store from "@/store";
import Header from "@/components/Header";

export default {
  name: "Home",
  props: {
    // Dictionary: key-month, value-records within that month
  },
  components: {
    mdbIcon,
    BarPlotChart,
    PiePlotChart,
    LinePlotChart,
    Dropdown,
    Header,
  },
  data() {
    return {
      loading: true,
      // Store all the cow ID
      cows: Array,
      // These three variables store all the data
      fat: Object,
      protein: Object,
      yield: Object,
      // These three variables sotre data in the current year
      fatData: Object,
      proteinData: Object,
      yieldData: Object,
      // Bind with dropdown options
      fatSelectedMonth: Number,
      proteinSelectedMonth: Number,
      yieldSelectedMonth: Number,
      profitSelectedMonth: Number,
      fatSelectedYear: String,
      proteinSelectedYear: String,
      yieldSelectedYear: String,
      // Calculate profitability
      price: 0.002,
      profitSelectedYear: String,
      years: Array,
      // For plotting pie charts
      thisYearTotalYield: Number,
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
      avgBarChartOptions: Object,
      yieldBarOptions: Object,
      profitBarOptions: Object,
      pieChartOptions: {
        hoverBorderWidth: 20,
        maintainAspectRatio: false,
      },
    };
  },
  created() {
    // Data from backend
    this.getHerdsData(this.$route.params.id);
    this.initOptions();
    this.initMonth(1);
  },
  mounted() {},
  updated() {},
  computed: {
    fatBarData: function() {
      const [key, val] = Object.entries(this.fatData)[
        this.fatSelectedMonth - 1
      ];

      return this.fillBarData(key, val, this.fatSelectedYear, "fat");
    },
    proteinBarData: function() {
      const [key, val] = Object.entries(this.proteinData)[
        this.proteinSelectedMonth - 1
      ];

      return this.fillBarData(key, val, this.proteinSelectedYear, "protein");
    },
    yieldBarData: function() {
      const [key, val] = Object.entries(this.yieldData)[
        this.yieldSelectedMonth - 1
      ];

      return this.fillBarData(key, val, this.yieldSelectedYear, "yield");
    },
    yieldPieData: function() {
      const [key, val] = Object.entries(this.yieldData)[
        this.yieldSelectedMonth - 1
      ];

      return this.fillPieData(key, val);
    },
    profitLineData: function() {
      var month = this.profitSelectedMonth - 1;
      var year = this.profitSelectedYear;
      // Fat
      var profitFatData = this.fat[year];
      const [fatKey, fatVal] = Object.entries(profitFatData)[month];
      // Protein
      var profitProteinData = this.protein[year];
      const [proteinKey, proteinVal] = Object.entries(profitProteinData)[month];
      // Yield
      var profitYieldData = this.yield[year];
      const [yieldKey, yieldVal] = Object.entries(profitYieldData)[month];
      var profitVal = this.calProfit(fatVal, proteinVal, yieldVal);
      console.log(fatKey, proteinKey, yieldKey);

      return this.fillBarData(fatKey, profitVal, year, "profit");
    },
    // Year list for dropdown options
    yearList: function() {
      var yearList = [];
      for (const id of this.years) {
        var tmp = {};
        tmp["id"] = id;
        tmp["name"] = id;
        yearList.push(tmp);
      }

      return yearList;
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
      this.thisYearTotalFat = this.sumArrays(this.fatData);
    },
    proteinSelectedYear: function(year) {
      this.proteinData = this.protein[year];
      this.thisYearTotalProtein = this.sumArrays(this.proteinData);
    },
    yieldSelectedYear: function(year) {
      this.yieldData = this.yield[year];
      this.thisYearTotalYield = this.sumArrays(this.yieldData);
    },
  },
  methods: {
    async getHerdsData(id) {
      var path = "/cow";
      var params = this.check(id);
      try {
        // console.log("send", params);
        const resp = await backend.fetchResource(path, params);
        // console.log(resp);
        this.years = resp["years"];
        this.cows = resp["cows"];
        this.fat = resp["fat_chart_data"];
        this.protein = resp["protein_chart_data"];
        this.yield = resp["milkyield_chart_data"];
        // Initialize selected year
        this.initYear(this.years[0]);
        // Initialize the current year data
        this.fatData = this.fat[this.fatSelectedYear];
        this.proteinData = this.protein[this.proteinSelectedYear];
        this.yieldData = this.yield[this.yieldSelectedYear];
        // Sum
        this.thisYearTotalYield = this.sumArrays(this.yieldData);
        // Set loading status
        this.loading = false;
      } catch (error) {
        console.log(error);
      }
    },
    // Check id
    check(id) {
      var email = store.getters.getUserEmail;
      var params = { email: email };
      // Number -100 means the whole herds
      params["ID"] = id === "-100" ? "all" : id;
      return params;
    },
    // Hanlde window
    handleUnload() {},
    // Fill bar charts data
    fillBarData(key, val, year, section) {
      var chartData = {};
      var datasets = [];
      var numOfDay = val.length;
      var labels = this.range(1, numOfDay);

      var tmpList = {};
      tmpList["label"] = key + "/" + year;
      var color;
      switch (section) {
        case "fat":
          color = "rgba(0, 153, 255, 0.7)";
          break;
        case "protein":
          color = "rgba(51, 51, 153, 0.7)";
          break;
        case "yield":
          color = "rgba(51, 153, 51, 0.7)";
          break;
        default:
          color = "rgba(255, 0, 0, 0.7)";
      }
      tmpList["backgroundColor"] = color;
      tmpList["data"] = val;

      datasets.push(tmpList);
      chartData["labels"] = labels;
      chartData["datasets"] = datasets;

      return chartData;
    },
    // Fill pie charts data
    fillPieData(key, val) {
      var chartData = {};
      var datasets = [];

      var labels;
      var totalVal;

      const currMonthStr = "Month " + key + " Yield";
      const totalStr = this.yieldSelectedYear + " Total Yield";
      labels = [currMonthStr, totalStr];
      totalVal = this.thisYearTotalYield;

      var tmpList = {};
      tmpList["label"] = key;
      tmpList["backgroundColor"] = [
        "rgba(65, 184, 131, 0.8)",
        "rgba(228, 103, 81, 0.8)",
      ];
      tmpList["data"] = [this.sumArray(val), totalVal];

      datasets.push(tmpList);
      chartData["labels"] = labels;
      chartData["datasets"] = datasets;

      return chartData;
    },
    // Yield * 453.6 * avg fat * price /pound
    // Yield * 453.6 * avg protein * price /pound
    // Fat: Array, Protein: Array, Yield: Array
    calProfit(fat, protein, yieldd) {
      var factor = 453.6;
      var price = this.price;
      var fp = fat.map((a, i) => a + protein[i]);
      var fpy = fp.map((a, i) => a * yieldd[i]);
      var singlePorfit = fpy.map((a) => a * price * factor);
      // console.log(singlePorfit);
      return singlePorfit;
    },
    // Initialize year
    initYear(year) {
      this.fatSelectedYear = year;
      this.proteinSelectedYear = year;
      this.yieldSelectedYear = year;
      this.profitSelectedYear = year;
    },
    // Initialize month to January
    initMonth(month) {
      this.fatSelectedMonth = month;
      this.proteinSelectedMonth = month;
      this.yieldSelectedMonth = month;
      this.profitSelectedMonth = month;
    },
    // Sum function
    // Items should be dictionary with {key-month, value-vals}
    sumArrays(items) {
      var vals = Object.values(items);
      var tmpSum = 0;
      for (const val of vals) {
        tmpSum += this.sumArray(val);
      }
      return tmpSum;
    },
    // Item should be an int array
    sumArray(item) {
      return item.reduce((a, b) => a + b, 0);
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
    handleYieldMonth(id) {
      this.yieldSelectedMonth = id;
    },
    handleYieldYear(id) {
      this.yieldSelectedYear = id;
    },
    handleProfitMonth(id) {
      this.profitSelectedMonth = id;
    },
    handleProfitYear(id) {
      this.profitSelectedYear = id;
    },
    // Initial chart options
    initOptions() {
      this.avgBarChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "Date",
              },
            },
          ],
          yAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "Percentage",
              },
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      };

      var valBarChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: "Date",
              },
            },
          ],
        },
      };
      // Deep copy
      this.yieldBarOptions = JSON.parse(JSON.stringify(valBarChartOptions));
      this.yieldBarOptions["scales"]["yAxes"] = [
        {
          scaleLabel: {
            display: true,
            labelString: "Amount / lb",
          },
          ticks: {
            beginAtZero: true,
          },
        },
      ];
      this.profitBarOptions = JSON.parse(JSON.stringify(valBarChartOptions));
      this.profitBarOptions["scales"]["yAxes"] = [
        {
          scaleLabel: {
            display: true,
            labelString: "Amount / dollar",
          },
          ticks: {
            beginAtZero: true,
          },
        },
      ];
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
  width: 100%;
  background: white;
  border-radius: 12px;
  margin-bottom: 2em;
}

.card.yield {
  width: 48%;
  height: auto;
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
