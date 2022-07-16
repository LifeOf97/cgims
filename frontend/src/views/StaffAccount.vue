<script setup>
/* eslint-disable */
import { ref } from 'vue';
import AppStaffLeftNav from '../components/AppStaffLeftNav.vue';
import AppStaffAvatar from '../components/AppStaffAvatar.vue';

// refs
const mobileNav = ref(false)
</script>

<template>
  <main class="w-full h-full min-h-full bg-white">
    <div class="relative">

      <div>
        <!-- start of nav for large screens -->
        <div class="hidden fixed top-0 left-0 h-full overflow-auto bg-slate-50 lg:block lg:w-3/12 xl:w-2/12">
          <AppStaffLeftNav />
        </div>
        <!-- end of nav for large screens -->

        <!-- start of nav for small screens -->
        <transition
          name="slide-in"
          enter-from-class="-translate-x-full opacity-0"
          enter-active-class="transition-all duration-200"
          leave-to-class="-translate-x-full opacity-0"
          leave-active-class="transition-all duration-200">
          <div v-if="mobileNav" class="fixed top-0 left-0 h-full w-9/12 z-40 shadow-lg overflow-auto bg-slate-50 lg:hidden">
            <AppStaffLeftNav ref="mobileNav" />
          </div>
        </transition>
        <!-- end of nav for small screens -->
      </div>

      <!-- start of routerview -->
      <div class="fixed right-0 w-full h-full bg-white overflow-auto lg:w-9/12 xl:w-10/12">
        <RouterView />

        <div class="absolute top-5 right-10">
          <AppStaffAvatar />
        </div>
      </div>
      <!-- end of routerview -->

    </div>

  </main>
</template>