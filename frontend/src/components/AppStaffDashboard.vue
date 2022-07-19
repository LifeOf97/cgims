<script setup>
/* eslint-disable */
import AppDashboardGreet from './AppDashboardGreet.vue';
import AppStaffDashboardCardHero from './AppStaffDashboardCardHero.vue';
import AppStaffDashboardQuestionnaires from './AppStaffDashboardQuestionnaires.vue';
import AppStaffCalendar from './AppStaffCalendar.vue';
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">
    <div class="relative w-full grid grid-cols-1 gap-7 lg:grid-cols-3">

        <div class="flex flex-col gap-7 lg:col-span-2">
            <AppDashboardGreet />
            <AppStaffDashboardCardHero />
            <AppStaffDashboardQuestionnaires class="mt-3" />
        </div>

        <div class="relative pb-10 lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffCalendar />
            </div>
        </div>
    </div>

  </main>
</template>