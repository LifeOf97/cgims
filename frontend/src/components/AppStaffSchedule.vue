<script setup>
/* eslint-disable */
import { computed, onBeforeMount } from 'vue';
import { useStaffScheduleStore } from '../stores/staffSchedule';
import AppStaffScheduleForm from "./AppStaffScheduleForm.vue";
import AppStaffCalendar from "./AppStaffCalendar.vue";
import AppStaffScheduleCard from "./AppStaffScheduleCard.vue";
import AppEmptyState from "./AppEmptyState.vue";
import IconInfoCircleOutline from './icons/IconInfoCircleOutline.vue';
import IconCalendar from './icons/IconCalendar.vue';

// stores
const scheduleStore = useStaffScheduleStore()

// computed
const calendarAttr = computed(() => {
    return [
        {
            key: 'today',
            highlight: 'red',
            dates: new Date(),
        },
        ...scheduleStore.retrieve.data.map(schedule => ({
            key: schedule.id,
            dates: schedule.expire,
            bar: 'blue',
            popover: {label: schedule.title}
        }))
    ]
})

// methods
const maxSchedule = () => {
    return scheduleStore.retrieve.data.length < 8
}

// hooks
onBeforeMount(() => {
  if (!scheduleStore.retrieve.data) scheduleStore.getQuestionnaires()
})
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="relative w-full grid grid-cols-1 gap-7 lg:grid-cols-3">

        <div class="flex flex-col gap-10 lg:col-span-2">
            <div>
                <!-- if max schedules reached -->
                <AppStaffScheduleForm v-if="maxSchedule()" />

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
                    <IconInfoCircleOutline
                        v-tippy="{arrow: true, animation: 'scale', maxWidth: '150px', theme: 'translucent', placement: 'left'}"
                        content="You can only have a maximum of 8 schedules"
                        class="w-6 h-6 fill-slate-400 transition-all duration-200 cursor-help hover:fill-slate-900 focus:outline-none" />
                </div>
                <div>
                    <!-- start of loading effect -->
                    <div v-if="scheduleStore.retrieve.loading" class="w-full grid gap-7 grid-cols-1 pb-10 sm:grid-cols-2 xl:grid-cols-3">
                        <div v-for="card in [1,2,3,4,5,6,7,8,9]" class="w-full h-32 bg-slate-100 shadow-md animate-pulse"></div>
                    </div>
                    <!-- end of loading effect -->

                    <!-- start of schedules card -->
                    <div v-else-if="scheduleStore.retrieve.data.length > 0" class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2">
                        <AppStaffScheduleCard v-for="schedule in scheduleStore.retrieve.data" :key="schedule.id" :schedule="schedule" />
                    </div>
                    <!-- end of schedules card -->

                    <!-- start of empty state -->
                    <AppEmptyState v-else>
                        <template #icon>
                            <IconCalendar class="w-10 h-10 fill-slate-200 md:w-16 md:h-16" />
                        </template>
                        <template #title>
                            <p class="text-slate-500 text-xs font-normal text-center md:text-sm">
                                You do not have any schedule
                            </p>
                        </template>
                        <template #tail><p></p></template>
                    </AppEmptyState>
                    <!-- end of empty state -->
                </div>
            </div>

        </div>

        <div class="w-full relative pb-10 lg:block lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffCalendar :attr="calendarAttr" />
            </div>
        </div>

    </div>

  </main>
</template>