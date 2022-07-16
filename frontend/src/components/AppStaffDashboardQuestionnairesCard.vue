<script setup>
/* eslint-disable */
import AppDoughnutChart from './AppDoughnutChart.vue';
import {DateTime} from "luxon";
import IconGroup from './icons/IconGroup.vue';
import IconClock from './icons/IconClock.vue';

// props
const props = defineProps({
    questionnaire: {
        type: Object,
        default: {
            data: {title: "Questionnaire title", students: 12, created: DateTime.now().setZone('Africa/Lagos')}
        }
    }
})

const humanizeDate = (value) => {
    return DateTime.fromISO(value).toRelative();
}

</script>

<template>
  <main class="relative w-full h-full bg-slate-50 shadow-md rounded-md">
    <div class="flex gap-5 py-6 px-4">

        <AppDoughnutChart class="w-20 h-20 self-start" />

        <div class="w-full flex-1 flex flex-col gap-2">
            <p class="text-slate-900 text-sm font-medium truncate md:text-lg">{{props.questionnaire.data.title}}</p>
            
            <div class="flex gap-5">
                <span class="flex gap-2">
                    <IconGroup class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{props.questionnaire.data.students}} Student(s)</p>
                </span>
                <span class="flex gap-2">
                    <IconClock class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{humanizeDate(props.questionnaire.data.created)}}</p>
                </span>
            </div>

            <!-- edit button -->
            <button
                class="w-full text-slate-900 font-medium py-2 mt-5 bg-white shadow-md rounded-lg transition-all duration-200
                ring-offset-2 ring-offset-slate-50 ring-rose-500 hover:ring-2 hover:bg-rose-500 hover:text-white">
                Edit
            </button>
            <!-- edit button -->
        </div>

    </div>
  </main>
</template>