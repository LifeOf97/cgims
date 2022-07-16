<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import AppLogo from './AppLogo.vue';
import IconDashboard from './icons/IconDashboard.vue';
import IconCalendar from './icons/IconCalendar.vue';
import IconGroup from './icons/IconGroup.vue';
import IconLogOut from './icons/IconLogOut.vue';
</script>

<template>
  <main class="w-full h-full bg-transparent pt-10 pb-5">
    <!-- start of nav for large screens -->
    <div class="w-full mx-auto h-full flex flex-col gap-16">
      <div class="pl-8">
          <AppLogo />
      </div>

      <div class="w-full h-full flex flex-col justify-between ">

        <div class="w-10/12 mx-auto flex flex-col gap-2">
          <RouterLink to="#" class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-rose-500">
            <IconDashboard class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
            <p class="text-xs text-slate-700 font-medium transition-all duration-200 group-hover:text-slate-50 md:text-sm">Dashboard</p>
          </RouterLink>
          <RouterLink to="#" class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-rose-500">
            <IconCalendar class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
            <p class="text-xs text-slate-700 font-medium transition-all duration-200 group-hover:text-slate-50 md:text-sm">My Schedules</p>
          </RouterLink>
          <RouterLink to="#" class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-rose-500">
            <IconGroup class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
            <p class="text-xs text-slate-700 font-medium transition-all duration-200 group-hover:text-slate-50 md:text-sm">My Students</p>
          </RouterLink>
        </div>

        <div class="w-full border-t border-slate-200 pt-5">
           <button type="button" @click.prevent class="w-10/12 mx-auto group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-rose-500">
              <IconLogOut class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
              <p class="text-xs text-slate-700 font-medium transition-all duration-200 group-hover:text-slate-50 md:text-sm">Sign Out</p>
            </button>
        </div>

      </div>
    </div>
    <!-- start of nav for large screens -->
  </main>
</template>