<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire'
import AppStaffDashboardQuestionnairesCard from './AppStaffDashboardQuestionnairesCard.vue'
import AppStaffQuestionnaireForm from './AppStaffQuestionnaireForm.vue';

// refs
const questionnaire = ref(false)

// stores
const questionnaireStore = useStaffQuestionnaireStore()
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">

    <div class="w-full h-full flex flex-col gap-10">
        <div class="w-full bg-white/50 backdrop-blur-lg border-b border-slate-200 pb-5 z-10">
            <p class="text-lg text-slate-900 font-semibold tracking-wider md:text-2xl">Questionnaires</p>
        </div>

        <div class="grid gap-7 grid-cols-1 pb-10 md:grid-cols-2 lg:grid-cols-3">
            <AppStaffDashboardQuestionnairesCard v-for="card in [1,2,3,4,5,6,7,8,9]" :key="card" />
            <button @click="questionnaireStore.create.open = true">Open Questionnaire</button>
        </div>

    </div>

    <teleport to="body">
        <transition
            name="scale"
            enter-from-class="scale-0 opacity-0"
            enter-active-class="transition-all duration-200"
            leave-to-class="scale-0 opacity-0"
            leave-active-class="transition-all duration-200">
            <div v-if="questionnaireStore.create.open || questionnaireStore.edit.open" class="w-full h-full overflow-auto">
                <AppStaffQuestionnaireForm />
            </div>
        </transition>
    </teleport>

  </main>
</template>