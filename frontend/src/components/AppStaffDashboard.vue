<script setup>
/* eslint-disable */
import { onBeforeMount, computed } from 'vue';
import { useUserStore } from '../stores/user';
import { useStaffQuestionnaireStore } from '../stores/staffQuestionnaire';
import { useStaffScheduleStore } from '../stores/staffSchedule';
import AppDashboardGreet from './AppDashboardGreet.vue';
import AppStaffDashboardCardHero from './AppStaffDashboardCardHero.vue';
import AppStaffDashboardQuestionnaires from './AppStaffDashboardQuestionnaires.vue';
import AppStaffCalendar from './AppStaffCalendar.vue';

// stores
const userStore = useUserStore()
const questionnaireStore = useStaffQuestionnaireStore()
const scheduleStore = useStaffScheduleStore()

// computed
const calendarAttr = computed(() => {
    return [
        {
            key: 'today',
            highlight: 'red',
            dates: new Date(),
        },
        ...scheduleStore.retrieve.data.map(schedule => ({
            key: schedule.id,
            dates: schedule.expire,
            bar: 'blue',
            popover: {label: schedule.title}
        }))
    ]
})

// hooks
onBeforeMount(() => {
  if (!userStore.userData.data) userStore.getMe()
  if (!questionnaireStore.retrieve.data) questionnaireStore.getQuestionnaires()
})
</script>

<template>
  <main class="w-full h-full bg-white px-5 pt-32 lg:pt-20">
    <div class="relative w-full grid grid-cols-1 gap-7 lg:grid-cols-3">

        <div class="flex flex-col gap-7 lg:col-span-2">
            <AppDashboardGreet :person="userStore.userData.data" />
            <AppStaffDashboardCardHero />
            <AppStaffDashboardQuestionnaires class="mt-3" />
        </div>

        <div class="relative pb-10 lg:pb-0">
            <div class="lg:mt-24 lg:sticky lg:top-3">
                <AppStaffCalendar :attr="calendarAttr" />
            </div>
        </div>
    </div>

  </main>
</template>