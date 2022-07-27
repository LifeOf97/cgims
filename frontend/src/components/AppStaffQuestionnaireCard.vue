<script setup>
/* eslint-disable */
import { computed, reactive } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import AppDoughnutChart from './AppDoughnutChart.vue';
import {DateTime} from "luxon";
import IconGroup from './icons/IconGroup.vue';
import IconClock from './icons/IconClock.vue';
import AppButton from './AppButton.vue';
import IconUserPlus from './icons/IconUserPlus.vue';

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

const viewQuestionnaire = () => {
    questionnaireStore.focus.data = props.questionnaire
    questionnaireStore.view.open = true
}

const updateQuestionnaire = () => {
    questionnaireStore.focus.data = props.questionnaire
    questionnaireStore.update.open = true
}

</script>

<template>
  <main class="relative w-full bg-slate-100 shadow-md rounded-md">
    <div class="w-full h-full mx-auto flex gap-5 px-4 py-4">
        
        <div class="flex items-center justify-center">
            <div v-if="props.questionnaire.students.length > 0" class="flex flex-col items-center justify-center gap-1">
                <AppDoughnutChart :chart-data="chartData" class="w-16 h-16 md:w-20 md:h-20" />
                <div class="flex flex-col items-center gap-1">
                    <p class="text-xs text-slate-500">Completed by</p>
                    <p class="text-xs text-green-500 font-medium">0/{{props.questionnaire.students.length}}</p>
                </div>
            </div>
            <div v-else class="flex flex-col items-center justify-center gap-2">
                <IconUserPlus class="w-10 h-10 fill-slate-300" />
                <p class="text-xs text-slate-500">Not Assigned</p>
            </div>
        </div>

        <div class="w-full h-full flex-1 flex flex-col gap-2 truncate">
            <p class="text-slate-900 text-sm font-medium truncate md:text-lg">{{props.questionnaire.title}}</p>
            
            <div class="w-full flex flex-wrap gap-2 xl:gap-5">
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
            <div class="pt-3 flex items-center gap-3">
                <AppButton class="w-full" @click.prevent="viewQuestionnaire()" label="View" :type="1" :color="1" />
                <AppButton class="w-full" @click.prevent="updateQuestionnaire()" label="Update" :type="1" :color="1" />
            </div>
            <!-- end view/edit button -->
        </div>

    </div>
  </main>
</template>