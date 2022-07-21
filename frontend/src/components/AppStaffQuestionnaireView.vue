<script setup>
/* eslint-disable */
import { DateTime } from 'luxon';
import { ref } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import { useUserStore } from '../stores/user';
import AppButton from './AppButton.vue';
import AppUserHandle from './AppUserHandle.vue';
import IconCloseBig from './icons/IconCloseBig.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()
const userStore = useUserStore()

// refs
const fullDate = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.DATE_FULL))

// datas
const tags = ['art', 'sss1', 'sss2', 'sss3']
</script>

<template>
  <main class="w-full h-full selection:bg-rose-500 selection:text-white">

    <div
      class="relative w-full h-auto mx-auto bg-white py-10 px-5 flex flex-col gap-16 shadow-lg shadow-slate-500/50 md:py-20 md:px-20 lg:w-10/12 xl:w-9/12">

      <div class="w-full h-full flex flex-col gap-7">

        <!-- start of title -->
        <h1 class="text-slate-900 text-xl font-bold mb-5 lg:text-3xl">This is the topic of the questionnaire</h1>
        <!-- end of title -->

        <!-- start of staff and date -->
        <div class="w-full flex items-center justify-between">
          <AppUserHandle :person="userStore.userData.data" />
          <p class="text-slate-500 text-xs font-medium md:text-sm">{{ fullDate }}</p>
        </div>
        <!-- end of staff and date -->

        <!-- start of questionnaire students categories as tags -->
        <div class="w-full flex items-center gap-2">
          <p v-for="tag in tags" :key="tag"
            class="text-xs text-slate-600 font-normal px-2 py-1 bg-slate-50 rounded-md">{{ tag }}</p>
        </div>
        <!-- end of questionnaire students categories as tags -->

        <!-- start of questions -->
        <div class="w-full p-2 bg-slate-50 rounded-md">
          <p class="text-slate-700 text-xs font-medium my-6 whitespace-pre-line md:text-sm">This is the text body</p>
        </div>
        <!-- end of questions -->

        <!-- start of buttons -->
        <div class="border-t border-slate-200 pt-5 flex items-center justify-end gap-2">
          <AppButton @click.prevent="questionnaireStore.delete.open = true" label="Delete" :type="1" :color="1" />
          <AppButton @click.prevent="questionnaireStore.view.open = false, questionnaireStore.update.open = true" label="Update" :type="2" :color="2" />
        </div>
        <!-- end of buttons -->

      </div>

      <button @click="questionnaireStore.view.open = false" type="button" class="absolute top-0 right-0 p-2 transition-all duration-200 rounded-md group hover:bg-slate-100">
        <IconCloseBig class="w-7 h-7 fill-slate-600 transition-all duration-200 group-hover:fill-rose-500" />
      </button>

    </div>
  </main>
</template>