<script setup>
/* eslint-disable */
import { ref } from 'vue';
import AppStaffStudentCard from './AppStaffStudentCard.vue'
import AppEmptyState from './AppEmptyState.vue';
import IconUserPlus from './icons/IconUserPlus.vue';

// refs
const hasStudents = ref(true)

// datas
const students = [
    { id: 1, firstName: "First1", lastName: "Last1", otherName: "Other1", mugshot: "", department: "Science", class: "sss2", regNo: "1231" },
    { id: 2, firstName: "First2", lastName: "Last2", otherName: "Other2", mugshot: "", department: "Science", class: "sss2", regNo: "1232" },
    { id: 3, firstName: "First3", lastName: "Last3", otherName: "Other3", mugshot: "", department: "Commercial ", class: "sss2", regNo: "1233" },
    { id: 4, firstName: "First4", lastName: "Last4", otherName: "Other4", mugshot: "", department: "Science", class: "sss2", regNo: "1234" },
    { id: 5, firstName: "First5", lastName: "Last5", otherName: "Other5", mugshot: "", department: "Science", class: "sss2", regNo: "1235" },
    { id: 6, firstName: "First6", lastName: "Last6", otherName: "Other6", mugshot: "", department: "Art", class: "sss2", regNo: "1236" },
    { id: 7, firstName: "First7", lastName: "Last7", otherName: "Other7", mugshot: "", department: "Social Science", class: "sss2", regNo: "1237" },
    { id: 8, firstName: "First8", lastName: "Last8", otherName: "Other8", mugshot: "", department: "Commercial", class: "sss2", regNo: "1238" },
    { id: 9, firstName: "First9", lastName: "Last9", otherName: "Other9", mugshot: "", department: "Art", class: "sss2", regNo: "1239" },
]
</script>

<template>
    <main class="w-full h-full bg-white flex flex-col gap-10">

        <div class="w-full border-b border-slate-200 pb-2 flex flex-col gap-1 backdrop-blur-lg z-20 sticky top-0">
            <h3 class="text-lg text-slate-900 font-semibold tracking-wider md:text-2xl">My students</h3>
            <p class="text-xs text-slate-400 font-medium">As assigned to you via the admin</p>
        </div>

        <div v-if="hasStudents" class="w-full h-full  grid gap-y-10 gap-x-5 pb-10 grid-cols-1 md:grid-cols-2 xl:grid-cols-4">
            <AppStaffStudentCard v-for="student in students" :key="student.id" :student="student" />
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