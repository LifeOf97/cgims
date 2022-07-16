<script setup>
/* eslint-disable */
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

// props
const props = defineProps({
    chartId: {type: String, default: 'bar-chart'},
    datasetIdKey: {type: String, default: 'label'},
    width: { type: Number, default: 400},
    height: { type: Number, default: 400},
    cssClasses: { default: '', type: String},
    styles: { type: Object, default: () => {}},
    plugins: { type: Object, default: () => {}}
})

// datas
const chart = {
    chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
    },
    chartOptions: {
        responsive: true
    }
}
</script>

<template>
  <main class="w-full h-full">
    <Bar
        :chart-options="chart.chartOptions"
        :chart-data="chart.chartData"
        :chart-id="props.chartId"
        :dataset-id-key="props.datasetIdKey"
        :plugins="props.plugins"
        :css-classes="props.cssClasses"
        :styles="props.styles"
        :width="props.width"
        :height="props.height"
    />
  </main>
</template>
