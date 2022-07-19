<script setup>
/* eslint-disable */
import { reactive } from 'vue';
import { DateTime } from 'luxon';
import AppStaffScheduleForm from "./AppStaffScheduleForm.vue";
import AppStaffCalendar from "./AppStaffCalendar.vue";
import AppStaffScheduleCard from "./AppStaffScheduleCard.vue";

// datas
const schedules = [
    {id: 1, completed: false, title: 'Title of schedule 1', detail: "Detail 1", created: DateTime.now()},
    {id: 2, completed: false, title: 'Title of schedule 2', detail: "Detail 2", created: DateTime.now()},
    {id: 3, completed: false, title: 'Title of schedule 3', detail: "Detail 3", created: DateTime.now()},
    {id: 4, completed: false, title: 'Title of schedule 4', detail: "Detail 4", created: DateTime.now()},
    {id: 5, completed: false, title: 'Title of schedule 5', detail: "Detail 5", created: DateTime.now()},
]
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="relative w-full grid grid-cols-1 gap-7 lg:grid-cols-3">

        <div class="col-span-2 flex flex-col gap-10">
            <AppStaffScheduleForm />

            <div class="w-full flex flex-col gap-7 pb-10">
                <div class="border-b border-slate-200 lg:sticky lg:top-0 lg:backdrop-blur">
                    <h3 class="text-slate-900 text-xl font-bold mb-5 md:text-2xl">My Schedules</h3>
                </div>
                <div class="grid grid-cols-1 gap-5 md:grid-cols-2">
                    <AppStaffScheduleCard v-for="schedule in schedules" :key="schedule.id" v-bind="schedule" />
                </div>
            </div>
        </div>

        <div class="relative pb-10 lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffCalendar />
            </div>
        </div>

    </div>

  </main>
</template>