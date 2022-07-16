<script setup>
/* eslint-disable */
import AppDashboardGreet from './AppDashboardGreet.vue';
import AppStaffDashboardCardHero from './AppStaffDashboardCardHero.vue';
import AppStaffDashboardQuestionnaires from './AppStaffDashboardQuestionnaires.vue';
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-20">
    <div class="relative w-full grid grid-cols-1 gap-4 lg:grid-cols-3">

        <div class="col-span-2 flex flex-col gap-7">
            <AppDashboardGreet />
            <AppStaffDashboardCardHero />
            <AppStaffDashboardQuestionnaires />
        </div>

        <div class="relative">
            <div class="lg:sticky lg:top-20">
                hhhe
            </div>
        </div>


    </div>
  </main>
</template>