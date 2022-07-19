<script setup>
/* eslint-disable */
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import AppDoughnutChart from './AppDoughnutChart.vue';
import {DateTime} from "luxon";
import IconGroup from './icons/IconGroup.vue';
import IconClock from './icons/IconClock.vue';
import AppButton from './AppButton.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()

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
    <div class="w-full flex gap-5 py-6 px-4">

        <AppDoughnutChart class="w-20 h-20 self-start" />

        <div class="w-full flex-1 flex flex-col gap-2">
            <p class="text-slate-900 text-sm font-medium truncate md:text-lg">{{props.questionnaire.data.title}}</p>
            
            <div class="flex flex-col gap-2 md:gap-5 md:flex-row">
                <span class="flex gap-2">
                    <IconGroup class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{props.questionnaire.data.students}} Student(s)</p>
                </span>
                <span class="flex gap-2">
                    <IconClock class="w-4 h-4 fill-slate-500" />
                    <p class="mt-px text-xs text-slate-500 font-medium">{{humanizeDate(props.questionnaire.data.created)}}</p>
                </span>
            </div>

            <!-- start view/edit button -->
            <div class="mt-5 flex items-center gap-3">
                <AppButton class="w-full" @click="questionnaireStore.view.open = true" label="View" :type="2" :color="1" />
                <AppButton class="w-full" @click="questionnaireStore.edit.open = true" label="Update" :type="2" :color="1" />
            </div>
            <!-- end view/edit button -->
        </div>

    </div>
  </main>
</template>