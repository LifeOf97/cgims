<script setup>
/* eslint-disable */
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

// props
const props = defineProps({
    chartId: {type: String, default: 'doughnut-chart'},
    datasetIdKey: {type: String, default: 'label'},
    width: { type: Number},
    height: { type: Number},
    cssClasses: { default: '', type: String},
    styles: { type: Object, default: () => {}},
    plugins: { type: Object, default: () => {}}
})

// datas
const chart = {
    chartData: {
        datasets: [
            {
                data: [10, 2],
                backgroundColor: ['#94a3b8', '#e2e8f0'],
                borderWidth: 4,
            }
        ]
    },
    chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {position: ""},
            title: {display: false, text: "Completed by"}
        }
    }
}
</script>

<template>
<Doughnut
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
</template>
