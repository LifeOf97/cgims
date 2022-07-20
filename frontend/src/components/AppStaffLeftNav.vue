<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';
import { ref, computed } from 'vue';
import AppLogo from './AppLogo.vue';
import AppButton from './AppButton.vue';
import IconCalendar from './icons/IconCalendar.vue';
import IconGroup from './icons/IconGroup.vue';
import IconLogOut from './icons/IconLogOut.vue';
import IconFolder from './icons/IconFolder.vue';
import IconHome from './icons/IconHome.vue';
import AppNotificationModal from './AppNotificationModal.vue';

// emits
const emits = defineEmits(['click'])

// route
const route = useRoute()

//refs
const signOut = ref(false)

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
           <button type="button" @click.prevent="signOut = true" class="w-10/12 mx-auto group flex items-center gap-3 p-2 rounded-md transition-all duration-200 hover:bg-slate-400">
              <IconLogOut class="w-6 h-6 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
              <p class="text-xs text-slate-700 font-medium transition-all duration-200 truncate group-hover:text-slate-50 md:text-sm">Sign Out</p>
            </button>
        </div>

      </div>
    </div>
    <!-- start of nav for large screens -->

    <teleport to="body">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="signOut" class="fixed w-full h-full z-50 flex items-end justify-center bg-slate-400/50 backdrop-blur overflow-auto md:items-center">
            <AppNotificationModal>
              <template #icon><IconLogOut class="w-7 h-7 fill-rose-500" /></template>
              <template #header>Sign Out</template>
              <template #detail>Are you sure you want to sign out?</template>
              <template #buttons>
                <AppButton class="w-full md:w-auto" @click.prevent="signOut = false" label="Cancle" :type="1" :color="1" />
                <AppButton class="w-full md:w-auto" @click.prevent label="Sign out" :type="2" :color="2" />
              </template>
            </AppNotificationModal>
          </div>
      </transition>
    </teleport>

  </main>
</template>