<script setup>
/* eslint-disable */
import { ref } from "vue";
import {DateTime} from "luxon";
import AppButton from "./AppButton.vue";
import IconFlag from './icons/IconFlag.vue'
import { useStaffScheduleStore } from "../stores/staffSchedule";

// stores
const scheduleStore = useStaffScheduleStore()

// refs
const open = ref(false)

// props
const props = defineProps({
    schedule: {type: Object}
})

// data
const schedulId = document.getElementsByClassName("detail")

// methods
const displayDate = (value) => {
    return DateTime.fromISO(value).setLocale("en-US").toLocaleString(DateTime.DATETIME_MED);
}
</script>

<template>
    <main class="detail">

        <details @click="open = !open" class="flex flex-col gap-4 bg-slate-100 rounded-md p-4 shadow transition-all duration-500 group open:shadow-lg hover:shadow-lg">
            <summary class="flex items-center gap-4 cursor-pointer">
                <IconFlag :class="props.schedule.completed ? 'fill-green-500':'fill-slate-400'" class="w-7 h-7 transition-all duration-200" />

                <span class="flex flex-col max-w-[80%]">
                    <p :class="open ? '':'truncate'" class="text-sm text-slate-700 font-medium">{{props.schedule.title}}</p>
                    <p class="text-xs text-slate-500 font-light">{{displayDate(props.schedule.created)}} </p>
                </span>
            </summary>

            <span class="flex flex-col gap-8 mt-4 ml-10">
                <p class="text-slate-700 text-sm font-normal">{{props.schedule.detail}}</p>

                <!-- buttons -->
                <div class="flex flex-wrap items-center justify-end border-t pt-2 md:gap-3">
                    <div class="flex flex-wrap gap-3 md:gap-1 xl:gap-3">
                        <AppButton class="md:w-full xl:w-auto" @click.prevent="scheduleStore.delete.open = true, scheduleStore.delete.id = props.schedule.id" label="Delete" :type="2" :color="2" />
                    </div>
                </div>
            </span>

        </details>

    </main>
</template>