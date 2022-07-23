<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import { useStaffScheduleStore } from '../stores/staffSchedule';
import { useUserStore } from '../stores/user';
import AppStaffLeftNav from '../components/AppStaffLeftNav.vue';
import AppUserHandle from '../components/AppUserHandle.vue';
import IconHamburger from '../components/icons/IconHamburger.vue';
import AppStaffQuestionnaireForm from '../components/AppStaffQuestionnaireForm.vue';
import AppStaffQuestionnaireView from '../components/AppStaffQuestionnaireView.vue';
import AppNotificationModal from '../components/AppNotificationModal.vue';
import AppButton from '../components/AppButton.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()
const scheduleStore = useStaffScheduleStore()
const userStore = useUserStore()

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
          <div v-if="mobileNav" class="fixed top-0 left-0 h-full w-full flex z-40 overflow-auto bg-transparent lg:hidden">
            <div class="fixed h-full overflow-auto w-9/12 bg-slate-100 shadow-lg shadow-black/50">
              <AppStaffLeftNav @click="mobileNav = false" />
            </div>
            <div @click="mobileNav = false" class="fixed right-0 h-full w-3/12 backdrop-blur"></div>
          </div>
        </transition>
        <!-- end of nav for small screens -->
      </div>

      <!-- start of routerview -->
      <div class="fixed right-0 w-full h-full bg-white overflow-auto lg:w-9/12 xl:w-10/12">
        
        <div class="w-full absolute px-5 top-5 right-0 flex items-center justify-between lg:justify-end">
          <button @click="mobileNav = true" type="button" class="group lg:hidden">
            <IconHamburger class="w-10 h-10 fill-slate-500 transition-all duration-200 group-hover:fill-rose-500" />
          </button>
          <AppUserHandle :person="userStore.userData.data" />
        </div>

        <div @click="mobileNav = false" class="w-full">
          <RouterView id="staffView" />
        </div>
      </div>
      <!-- end of routerview -->

    </div>

    <!-- start of questionnaire form modal -->
    <teleport to="#app">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="questionnaireStore.create.open||questionnaireStore.update.open" class="fixed w-full h-full z-20 bg-slate-400/50 backdrop-blur overflow-auto">
            <AppStaffQuestionnaireForm />
          </div>
      </transition>
    </teleport>
    <!-- end of questionnaire form modal -->

    <!-- start of questionnaire view modal -->
    <teleport to="#app">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="questionnaireStore.view.open" class="fixed w-full h-full z-20 bg-slate-400/50 backdrop-blur overflow-auto">
            <AppStaffQuestionnaireView />
          </div>
      </transition>
    </teleport>
    <!-- end of questionnaire view modal -->

    <!-- start of questionnaire delete modal -->
    <teleport to="#app">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="questionnaireStore.delete.open" class="fixed w-full h-full z-30 flex items-end justify-center bg-slate-400/50 backdrop-blur overflow-auto md:items-center">
            <AppNotificationModal>
              <template #header>Delete questionnaire</template>
              <template #detail>Are you sure you want to delete this questionnaire?</template>
              <template #buttons>
                <AppButton class="w-full md:w-auto" @click.prevent="questionnaireStore.delete.open = false" label="Cancle" :type="1" :color="1" />
                <AppButton class="w-full md:w-auto" @click.prevent="questionnaireStore.deleteQuestionnaire()" label="Delete" :type="2" :color="2" :loading="questionnaireStore.delete.loading" />
              </template>
            </AppNotificationModal>
          </div>
      </transition>
    </teleport>
    <!-- end of questionnaire delete modal -->

    <!-- start of schedule delete modal -->
    <teleport to="#app">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="scheduleStore.delete.open" class="fixed w-full h-full z-30 flex items-end justify-center bg-slate-400/50 backdrop-blur overflow-auto md:items-center">
            <AppNotificationModal>
              <template #header>Delete schedule</template>
              <template #detail>Are you sure you want to delete this schedule?</template>
              <template #buttons>
                <AppButton class="w-full md:w-auto" @click.prevent="scheduleStore.delete.open = false" label="Cancle" :type="1" :color="1" />
                <AppButton class="w-full md:w-auto" @click.prevent="scheduleStore.deleteSchedule()" label="Delete" :type="2" :color="2" :loading="scheduleStore.delete.loading" />
              </template>
            </AppNotificationModal>
          </div>
      </transition>
    </teleport>
    <!-- end of schedule delete modal -->

  </main>
</template>