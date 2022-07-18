<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import AppStaffDashboardQuestionnairesCard from './AppStaffDashboardQuestionnairesCard.vue'
import IconLongRight from './icons/IconLongRight.vue';
import IconLongLeft from './icons/IconLongLeft.vue';
</script>

<template>
  <main class="w-full h-full bg-white pb-0 lg:pb-10">

    <div class="w-full h-full flex flex-col gap-10">
        <div class="w-full bg-white/50 backdrop-blur-lg border-b border-slate-200 pb-5 flex flex-col gap-1">
          <p class="text-lg text-slate-900 font-medium tracking-wider md:text-xl">Questionnaires</p>
          <p class="text-xs text-slate-500 font-normal">Based on recently created</p>
        </div>

        <div class="grid gap-5 grid-cols-1 md:grid-cols-2">
            <AppStaffDashboardQuestionnairesCard v-for="card in [1,2,3,4]" :key="card" />
        </div>

        <div class="w-full flex items-center gap-2">
          <div class="w-full h-px bg-slate-200"></div>
          <div class="flex shrink-0 items-center gap-2 group">
            <IconLongLeft class="w-7 h-7 fill-slate-400 group-hover:animate-bounce-left" />
            <RouterLink :to="{name: 'staffquestionnaires'}" class="text-blue-500 text-xs font-medium md:text-sm">View all</RouterLink>
          </div>
        </div>

    </div>

  </main>
</template>