<script setup>
/* eslint-disable */
import AppStaffDashboardQuestionnairesCard from './AppStaffDashboardQuestionnairesCard.vue'
</script>

<template>
  <main class="w-full h-full bg-white">

    <div class="w-full h-full flex flex-col gap-10">
        <div class="sticky top-0 w-full bg-white/50 backdrop-blur-lg border-b border-slate-200 pb-5 z-10">
            <p class="text-lg text-slate-700 font-medium tracking-wider md:text-xl">Questionnaires</p>
        </div>

        <div class="grid gap-5 pb-10 grid-cols-1 md:grid-cols-2">
            <AppStaffDashboardQuestionnairesCard v-for="card in [1,2,3,4,5,6,7,8,9]" :key="card" />
        </div>
    </div>

  </main>
</template>