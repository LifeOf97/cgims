<script setup>
/* eslint-disable */
import AppStaffDashboardQuestionnairesCard from './AppStaffDashboardQuestionnairesCard.vue'
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="w-full h-full flex flex-col gap-10">
        <div class="w-full bg-white/50 backdrop-blur-lg border-b border-slate-200 pb-5 z-10">
            <p class="text-lg text-slate-900 font-semibold tracking-wider md:text-2xl">Questionnaires</p>
        </div>

        <div class="grid gap-7 grid-cols-1 pb-10 md:grid-cols-2 xl:grid-cols-3">
            <AppStaffDashboardQuestionnairesCard v-for="card in [1,2,3,4,5,6,7,8,9]" :key="card" />
        </div>

    </div>

  </main>
</template>