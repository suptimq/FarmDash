export default {
  // Fill Bar chart data
  fillBarData() {
    var chartData = {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "Data One",
          backgroundColor: "#f87979",
          data: [40, 39, 10, 40, 39, 80, 40],
        },
      ],
    };

    var chartOptions = {
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
    };

    return [chartData, chartOptions];
  },

  // Fill Pie chart data
  fillPieData() {
    var chartOptions = {
      hoverBorderWidth: 20,
      maintainAspectRatio: false,
    };

    var chartData = {
      hoverBackgroundColor: "red",
      hoverBorderWidth: 10,
      labels: ["Green", "Red", "Blue"],
      datasets: [
        {
          label: "Data One",
          backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
          data: [1, 10, 5],
        },
      ],
    };

    return [chartData, chartOptions];
  },
};
