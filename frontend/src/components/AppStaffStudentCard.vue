<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import IconUser from './icons/IconUser.vue';
import IconAcademicAlt from './icons/IconAcademicAlt.vue';
import IconGroup from './icons/IconGroup.vue';
import IconIdCard from './icons/IconIdCard.vue';

const props = defineProps({
    firstName: {type: String, default: "First"},
    lastName: {type: String, default: "Last"},
    otherName: {type: String, default: "Other"},
    mugshot: {type: String, default: ""},
    department: {type: String, default: "Department"},
    class: {type: String, default: "jss1"},
    regNo: {type: String, default: "1234"},
})
</script>

<template>
  <main class="w-full h-full rounded-lg overflow-hidden shado bg-slate-100 border border-slate-300 duration-1000 hover:shadow-lg">

    <div class="flex flex-col group">

        <div class="w-full h-40 bg-slate-50 overflow-hidden">
            <div class="w-full h-full  duration-1000 group-hover:scale-125">
                <img v-if="props.mugshot" :src="props.mugshot" alt="image" class="w-full h-full object-cover object-center">
                <IconUser v-else class="w-full h-full fill-slate-200" />
            </div>
        </div>

        <div class="flex flex-col gap-5 p-4 bg-slate-100">
            <h3 class="text-sm text-slate-700 font-medium md:text-base truncate">{{props.firstName}} {{props.lastName}} {{props.otherName}}</h3>

            <div class="flex flex-col gap-1">
                <span class="flex items-center gap-4">
                    <IconGroup class="w-6 h-6 fill-slate-400" />
                    <p class="text-xs text-slate-400 font-normal capitalize md:text-sm">{{props.department}}</p>
                </span>
                <span class="flex items-center gap-4">
                    <IconAcademicAlt class="w-6 h-6 fill-transparent stroke-slate-400" />
                    <p class="text-xs text-slate-400 font-normal uppercase md:text-sm">{{props.class}}</p>
                </span>
                <span class="flex items-center gap-4">
                    <IconIdCard class="w-6 h-6 fill-slate-400" />
                    <p class="text-xs text-slate-400 font-normal md:text-sm">{{props.regNo}}</p>
                </span>
            </div>
        </div>

        <div class="w-11/12 mx-auto py-2">
            <RouterLink :to="{name: 'staffstudentsdata'}" class="w-full px-4 py-2 text-center text-sm rounded transition-all duration-200 shadow-lg disabled:cursor-wait md:text-base">
                View Student
            </RouterLink>
        </div>

    </div>

  </main>
</template>