<script setup>
/* eslint-disable */
import AppStaffScheduleForm from "./AppStaffScheduleForm.vue";
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="relative w-full grid grid-cols-1 gap-4 lg:grid-cols-3">

        <div class="col-span-2 flex flex-col gap-7">
            <AppStaffScheduleForm />
        </div>

        <div class="relative pb-10 lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffDashboardCalendar />
            </div>
        </div>

    </div>

  </main>
</template>