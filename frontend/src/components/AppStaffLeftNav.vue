<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';
import { computed } from 'vue';
import { useUserStore } from '../stores/user';
import AppLogo from './AppLogo.vue';
import IconCalendar from './icons/IconCalendar.vue';
import IconGroup from './icons/IconGroup.vue';
import IconFolder from './icons/IconFolder.vue';
import IconHome from './icons/IconHome.vue';
import IconLogOut from './icons/IconLogOut.vue';

// emits
const emits = defineEmits(['click'])

// route
const route = useRoute()

// stores
const userStore = useUserStore()

// computed
const isStudentRoute = computed(() => {
  return route.path.includes('students')
})
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

          <RouterLink
            @click="$emit('click')"
            :to="{name: 'staff'}"
            :class="route.name == 'staffdashboard' ? 'bg-slate-400':'bg-transparent'"
            class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconHome :class="route.name == 'staffdashboard' ? 'fill-white':'fill-slate-900'" class="w-6 h-6 transition-all duration-200 group-hover:fill-white" />
              <p :class="route.name == 'staffdashboard' ? 'text-slate-50':'text-slate-700'" class="text-xs font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">Dashboard</p>
          </RouterLink>

          <RouterLink
            @click="$emit('click')"
            :to="{name: 'staffquestionnaires'}"
            :class="route.name == 'staffquestionnaires' ? 'bg-slate-400':'bg-transparent'"
            class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconFolder :class="route.name == 'staffquestionnaires' ? 'fill-white':'fill-slate-900'" class="w-6 h-6 transition-all duration-200 group-hover:fill-white" />
              <p :class="route.name == 'staffquestionnaires' ? 'text-slate-50':'text-slate-700'" class="text-xs font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">My Questionnaires</p>
          </RouterLink>

          <RouterLink
            @click="$emit('click')"
            :to="{name: 'staffschedules'}"
            :class="route.name == 'staffschedules' ? 'bg-slate-400':'bg-transparent'"
            class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconCalendar :class="route.name == 'staffschedules' ? 'fill-white':'fill-slate-900'" class="w-6 h-6 transition-all duration-200 group-hover:fill-white" />
              <p :class="route.name == 'staffschedules' ? 'text-slate-50':'text-slate-700'" class="text-xs font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">My Schedules</p>
          </RouterLink>
          
          <RouterLink
            @click="$emit('click')"
            :to="{name: 'staffstudents'}"
            :class="isStudentRoute ? 'bg-slate-400':'bg-transparent'"
            class="group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconGroup :class="isStudentRoute ? 'fill-white':'fill-slate-900'" class="w-6 h-6 transition-all duration-200 group-hover:fill-white" />
              <p :class="isStudentRoute ? 'text-slate-50':'text-slate-700'"  class="text-xs font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">My Students</p>
          </RouterLink>
        </div>

        <div class="w-full border-t border-slate-200 pt-5">
           <button type="button" @click.prevent="userStore.userSignOut.open = true" class="w-10/12 mx-auto group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconLogOut class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
              <p class="text-xs text-slate-700 font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">Sign Out</p>
            </button>
        </div>

      </div>
    </div>
    <!-- start of nav for large screens -->

  </main>
</template>