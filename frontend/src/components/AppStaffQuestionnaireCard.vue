<script setup>
/* eslint-disable */
import { computed, reactive } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import AppDoughnutChart from './AppDoughnutChart.vue';
import {DateTime} from "luxon";
import IconGroup from './icons/IconGroup.vue';
import IconClock from './icons/IconClock.vue';
import AppButton from './AppButton.vue';

// props
const props = defineProps({
    questionnaire: {type: Object}
})

// stores
const questionnaireStore = useStaffQuestionnaireStore()


// reactive/refs
const chartData = reactive({
    datasets: [
        {
            data: [0, props.questionnaire.students.length],
            backgroundColor: ['#94a3b8', '#e2e8f0'],
            borderWidth: 4,
        }
    ],
})

// methods
const humanizeDate = (value) => {
    return DateTime.fromISO(value).toRelative();
}

const nunberOfStudents = () => {
    return props.questionnaire.students
}

</script>

<template>
  <main class="relative w-full h-full bg-slate-50 shadow-md rounded-md">
    <div class="w-full flex gap-5 py-6 px-4">
        
        <div class="flex flex-col gap-1 items-center">
            <AppDoughnutChart :chart-data="chartData" class="w-20 h-20 self-start" />
            <div class="flex flex-col items-center gap-1">
                <p class="text-xs text-slate-500">Completed by</p>
                <p class="text-xs text-slate-700 font-medium">0/{{props.questionnaire.students.length}}</p>
            </div>
        </div>

        <div class="w-full flex-1 flex flex-col gap-2">
            <p class="text-slate-900 text-sm font-medium truncate md:text-lg">{{props.questionnaire.title}}</p>
            
            <div class="flex flex-wrap gap-2 md:gap-5 lg:gap-2 xl:gap-5">
                <span class="flex gap-2">
                    <IconGroup class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{props.questionnaire.students.length}} Student(s)</p>
                </span>
                <span class="flex gap-2">
                    <IconClock class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{humanizeDate(props.questionnaire.created)}}</p>
                </span>
            </div>

            <!-- start view/edit button -->
            <div class="mt-5 flex items-center gap-3">
                <AppButton class="w-full" @click.prevent="questionnaireStore.view.open = true" label="View" :type="2" :color="1" />
                <AppButton class="w-full" @click.prevent="questionnaireStore.update.open = true" label="Update" :type="2" :color="1" />
            </div>
            <!-- end view/edit button -->
        </div>

    </div>
  </main>
</template>