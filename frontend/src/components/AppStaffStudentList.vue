<script setup>
/* eslint-disable */
import { ref, onBeforeMount} from 'vue';
import { useStudentStore } from '../stores/staffStudents';
import AppStaffStudentCard from './AppStaffStudentCard.vue'
import AppEmptyState from './AppEmptyState.vue';
import IconUserPlus from './icons/IconUserPlus.vue';

// stores
const studentStore = useStudentStore()

// hooks
onBeforeMount(() => {
  if (!studentStore.retrieve.data) studentStore.getStudents()
})
</script>

<template>
    <main class="w-full h-full bg-white flex flex-col gap-10">

        <div class="w-full border-b border-slate-200 pb-2 flex flex-col gap-1 backdrop-blur-lg z-20 sticky top-0">
            <h3 class="text-lg text-slate-900 font-semibold tracking-wider md:text-2xl">My students</h3>
            <p class="text-xs text-slate-400 font-medium">As assigned to you by the admin</p>
        </div>

        <div v-if="studentStore.retrieve.data.length > 0" class="w-full h-full  grid gap-y-10 gap-x-5 pb-10 grid-cols-1 md:grid-cols-2 xl:grid-cols-4">
            <AppStaffStudentCard v-for="student in studentStore.retrieve.data" :key="student.id" :student="student" />
        </div>

        <div v-else class="w-full mx-auto md:w-7/12">
            <AppEmptyState>
                <template #icon>
                    <IconUserPlus class="w-10 h-10 fill-slate-300 md:w-16 md:h-16" />
                </template>
                <template #title>
                    <p class="text-slate-500 text-xs font-normal text-center md:text-sm">
                        You are yet to be assigned students
                    </p>
                </template>
                <template #tail>
                    <p class="text-slate-400 text-xs font-light text-center md:text-sm">
                        Please contact the admin
                    </p>
                </template>
            </AppEmptyState>
        </div>

    </main>
</template>