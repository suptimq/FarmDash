import { generateChart, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

const BarPlot = generateChart("bar", "bar");

export default {
  extends: BarPlot,
  mixins: [reactiveProp],
  props: ["options"],
  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options);
  },
};
