<script setup>
/* eslint-disable */
import { computed } from 'vue';
import { DateTime } from 'luxon';
import AppStaffScheduleForm from "./AppStaffScheduleForm.vue";
import AppStaffCalendar from "./AppStaffCalendar.vue";
import AppStaffScheduleCard from "./AppStaffScheduleCard.vue";
import AppEmptyState from "./AppEmptyState.vue";
import IconHelpCircleOutline from "./icons/IconHelpCircleOutline.vue";
import IconInfoCircleOutline from './icons/IconInfoCircleOutline.vue';

// datas
const schedules = [
    {id: 1, completed: false, title: 'Title of schedule 1', detail: "Detail 1", created: DateTime.now()},
    {id: 2, completed: false, title: 'Title of schedule 2', detail: "Detail 2", created: DateTime.now()},
    {id: 3, completed: false, title: 'Title of schedule 3', detail: "Detail 3", created: DateTime.now()},
    {id: 4, completed: false, title: 'Title of schedule 4', detail: "Detail 4", created: DateTime.now()},
    {id: 5, completed: false, title: 'Title of schedule 5', detail: "Detail 5", created: DateTime.now()},
    {id: 6, completed: false, title: 'Title of schedule 6', detail: "Detail 6", created: DateTime.now()},
    {id: 7, completed: false, title: 'Title of schedule 7', detail: "Detail 7", created: DateTime.now()},
    {id: 8, completed: false, title: 'Title of schedule 8', detail: "Detail 8", created: DateTime.now()},
]

// computed
const maxSchedules = computed(() => {
    if (schedules.length < 8) return true
    else return false
})
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="relative w-full grid grid-cols-1 gap-7 lg:grid-cols-3">

        <div class="flex flex-col gap-10 lg:col-span-2">
            <div>
                <!-- if max schedules reached -->
                <AppStaffScheduleForm v-if="maxSchedules" />

                <!-- else -->
                <AppEmptyState v-else>
                    <template #icon>
                        <IconInfoCircleOutline class="w-10 h-10 fill-slate-200 md:w-16 md:h-16" />
                    </template>
                    <template #title>
                        <p class="text-slate-500 text-xs font-normal text-center md:text-sm">
                            You have reached your maximum schedule limit
                        </p>
                    </template>
                    <template #tail>
                        <p class="text-slate-400 text-xs font-light text-center md:text-sm">
                            Delete one or more schedules to create space
                        </p>
                    </template>
                </AppEmptyState>
            </div>

            <div class="w-full flex flex-col gap-7 pb-10">
                <div class="flex items-center justify-between border-b border-slate-200 pb-5 lg:sticky lg:top-0 lg:backdrop-blur">
                    <h3 class="text-slate-900 text-xl font-bold md:text-2xl">My Schedules</h3>
                    <IconHelpCircleOutline
                        v-tippy="{arrow: true, animation: 'scale', maxWidth: '150px', theme: 'translucent', placement: 'left'}"
                        content="You can only have a maximum of 8 schedules"
                        class="w-6 h-6 fill-slate-400 transition-all duration-200 cursor-help hover:fill-slate-900" />
                </div>
                <div class="grid grid-cols-1 gap-5 md:grid-cols-3 lg:grid-cols-2">
                    <AppStaffScheduleCard v-for="schedule in schedules" :key="schedule.id" v-bind="schedule" />
                </div>
            </div>
        </div>

        <div class="w-full relative pb-10 lg:block lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffCalendar />
            </div>
        </div>

    </div>

  </main>
</template>