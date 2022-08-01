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

// methods
const toFullDate = (value) => {
  return DateTime.fromISO(value).setLocale("en-US").toLocaleString(DateTime.DATE_FULL)
}

const updateQuestionnaire = () => {
    questionnaireStore.view.open = false
    questionnaireStore.update.open = true
}
</script>

<template>
  <main class="w-full h-full selection:bg-rose-500 selection:text-white">

    <div
      class="relative w-full h-auto mx-auto bg-white py-10 px-5 flex flex-col gap-16 shadow-lg shadow-slate-500/50 md:py-20 md:px-20 lg:w-10/12 xl:w-9/12">

      <div class="w-full h-full flex flex-col gap-7">

        <!-- start of title -->
        <h1 class="text-slate-900 text-xl font-bold mb-5 underline lg:text-3xl">{{questionnaireStore.focus.data.title}}</h1>
        <!-- end of title -->

        <!-- start of staff and date -->
        <div class="w-full flex items-center justify-between">
          <AppUserHandle :person="userStore.userData.data" />
          <p class="text-slate-500 text-xs font-medium md:text-sm">{{ toFullDate(questionnaireStore.focus.data.created) }}</p>
        </div>
        <!-- end of staff and date -->

        <!-- start of questionnaire students categories as tags -->
        <div class="w-full flex flex-wrap items-center gap-2">
          <p v-for="tag in questionnaireStore.focus.data.categories" :key="tag"
            class="text-xs text-slate-600 font-normal px-2 py-1 bg-slate-100 rounded-md">{{ tag.split('_').join(' ') }}</p>
        </div>
        <!-- end of questionnaire students categories as tags -->

        <!-- start of questions -->
        <div class="w-full p-2 border-t border-slate-200 pt-5">
          <p class="text-slate-700 text-xs font-medium my-6 whitespace-pre-line md:text-sm">{{questionnaireStore.focus.data.question}}</p>
        </div>
        <!-- end of questions -->

        <!-- start of buttons -->
        <div class="border-t border-slate-200 pt-5 flex items-center justify-end gap-2">
          <AppButton @click.prevent="questionnaireStore.delete.open = true" label="Delete" :type="1" :color="1" />
          <AppButton @click.prevent="updateQuestionnaire()" label="Update" :type="2" :color="2" />
        </div>
        <!-- end of buttons -->

      </div>

      <button @click="questionnaireStore.$reset()" type="button" class="absolute top-0 right-0 p-2 transition-all duration-200 rounded-md group hover:bg-slate-100">
        <IconCloseBig class="w-7 h-7 fill-slate-600 transition-all duration-200 group-hover:fill-rose-500" />
      </button>

    </div>
  </main>
</template>