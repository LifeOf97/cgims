<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import AppStaffLeftNav from '../components/AppStaffLeftNav.vue';
import AppStaffAvatar from '../components/AppStaffAvatar.vue';
import IconHamburger from '../components/icons/IconHamburger.vue';
import AppStaffQuestionnaireForm from '../components/AppStaffQuestionnaireForm.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()

// refs
const mobileNav = ref(false)
</script>

<template>
  <main class="w-full h-full min-h-full">
    <div class="relative">

      <div>
        <!-- start of nav for large screens -->
        <div class="hidden fixed top-0 left-0 h-full overflow-auto bg-slate-100 lg:block lg:w-3/12 xl:w-2/12">
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
          <div v-if="mobileNav" class="fixed top-0 left-0 h-full w-9/12 z-40 shadow-lg shadow-black/50 overflow-auto bg-slate-100 lg:hidden">
            <AppStaffLeftNav @click="mobileNav = false" />
          </div>
        </transition>
        <!-- end of nav for small screens -->
      </div>

      <!-- start of routerview -->
      <div :class="mobileNav ? 'blur-sm':'lg:blur-0'" class="fixed right-0 w-full h-full bg-white overflow-auto lg:w-9/12 xl:w-10/12">
        
        <div class="w-full absolute px-5 top-5 right-0 flex items-center justify-between lg:justify-end">
          <button @click="mobileNav = true" type="button" class="group lg:hidden">
            <IconHamburger class="w-10 h-10 fill-slate-500 transition-all duration-200 group-hover:fill-rose-500" />
          </button>
          <AppStaffAvatar  />
        </div>

        <div @click="mobileNav = false" class="w-full">
          <RouterView id="staffView" />
        </div>
      </div>
      <!-- end of routerview -->

    </div>

    <teleport to="body">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="questionnaireStore.create.open|questionnaireStore.edit.open" class="fixed w-full h-full z-50 bg-slate-400/50 backdrop-blur overflow-auto">
            <AppStaffQuestionnaireForm />
          </div>
      </transition>
    </teleport>

  </main>
</template>