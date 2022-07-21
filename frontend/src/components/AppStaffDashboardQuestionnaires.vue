<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import { ref } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import AppStaffQuestionnaireCard from './AppStaffQuestionnaireCard.vue'
import IconLongLeft from './icons/IconLongLeft.vue';
import AppEmptyState from './AppEmptyState.vue';
import IconFolderPlus from './icons/IconFolderPlus.vue';
import AppButton from './AppButton.vue';

// stores
const questionnaireStore = useStaffQuestionnaireStore()

// refs
const hasQuestionnaire = ref(true)
</script>

<template>
  <main class="w-full h-full bg-white pb-0 lg:pb-10">

    <div class="w-full h-full flex flex-col gap-10">
        <div class="w-full bg-white/50 backdrop-blur-lg border-b border-slate-200 pb-5 flex flex-col gap-1">
          <p class="text-lg text-slate-900 font-medium tracking-wider md:text-xl">Questionnaires</p>
          <p class="text-xs text-slate-500 font-normal">Based on recently created</p>
        </div>

        <!-- shows only if the staff has some questionnaires -->
        <div v-if="hasQuestionnaire" class="grid gap-5 grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-2">
            <AppStaffQuestionnaireCard v-for="card in [1,2,3,4]" :key="card" />
        </div>

        <!-- shows only if the staff has no questionnaires -->
        <AppEmptyState v-else>
          <template #icon>
            <IconFolderPlus class="w-10 h-10 fill-slate-200 md:w-16 md:h-16" />
          </template>
          <template #title>
            <p class="text-slate-500 text-xs font-medium text-center md:text-sm">
              You have not created any questionnaires.
            </p>
          </template>
          <template #tail>
            <div class="flex items-center justify-center mt-3">
              <AppButton @click="questionnaireStore.create.open = true" label="Create" :type="2" :color="3" />
            </div>
          </template>
        </AppEmptyState>

        <!-- shows only if the staff has some questionnaires -->
        <div v-if="hasQuestionnaire" class="w-full flex items-center gap-2">
          <div class="w-full h-px bg-slate-200"></div>
          <div class="flex shrink-0 items-center gap-2 group">
            <IconLongLeft class="w-7 h-7 fill-slate-400 group-hover:animate-bounce-left" />
            <RouterLink :to="{name: 'staffquestionnaires'}" class="text-blue-500 text-xs font-medium md:text-sm">View all</RouterLink>
          </div>
        </div>

    </div>

  </main>
</template>