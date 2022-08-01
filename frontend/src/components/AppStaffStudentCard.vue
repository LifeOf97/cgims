<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import { useStudentStore } from '../stores/staffStudents';
import IconUser from './icons/IconUser.vue';
import IconAcademicAlt from './icons/IconAcademicAlt.vue';
import IconGroup from './icons/IconGroup.vue';
import IconIdCard from './icons/IconIdCard.vue';

// props
const props = defineProps({
    student: {type: Object}
})

// stores
const studentStore = useStudentStore()
</script>

<template>
  <main class="w-full h-full rounded-lg overflow-hidden bg-slate-100 border border-slate-300 duration-1000 hover:shadow-lg">

    <div class="flex flex-col group">

        <div class="w-full h-40 bg-slate-50 overflow-hidden">
            <div class="w-full h-full  duration-1000 group-hover:scale-125">
                <img v-if="props.student.profile.image" :src="props.student.profile.image" alt="image" class="w-full h-full object-cover object-center">
                <IconUser v-else class="w-full h-full fill-slate-200" />
            </div>
        </div>

        <div class="flex flex-col gap-5 p-4 bg-slate-100">
            <h3 class="text-sm text-slate-700 font-medium md:text-base truncate">{{props.student.profile.first_name}} {{props.student.profile.last_name}} {{props.student.profile.other_name}}</h3>

            <div class="flex flex-col gap-1">
                <span class="flex items-center gap-4">
                    <IconGroup class="w-6 h-6 fill-slate-400" />
                    <p class="text-xs text-slate-400 font-normal capitalize md:text-sm">{{props.student.department.split('_').join(' ')}}</p>
                </span>
                <span class="flex items-center gap-4">
                    <IconAcademicAlt class="w-6 h-6 fill-transparent stroke-slate-400" />
                    <p class="text-xs text-slate-400 font-normal uppercase md:text-sm">{{props.student.level}}</p>
                </span>
                <span class="flex items-center gap-4">
                    <IconIdCard class="w-6 h-6 fill-slate-400" />
                    <p class="text-xs text-slate-400 font-normal md:text-sm">{{props.student.reg_no}}</p>
                </span>
            </div>
        </div>

        <div class="w-11/12 mx-auto py-2 flex">
            <RouterLink
                @click="studentStore.focus.data = student"
                :to="{name: 'staffstudentsdata', params: {department: props.student.department, class: props.student.level, regNo: props.student.reg_no}}"
                class="w-full px-4 py-2 text-center text-white text-sm rounded bg-slate-400 transition-all duration-1000 shadow-lg hover:bg-slate-600 md:text-base">
                View Student
            </RouterLink>
        </div>

    </div>

  </main>
</template>