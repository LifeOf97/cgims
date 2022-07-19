<script setup>
/* eslint-disable */
import { DateTime } from 'luxon';
import AppStaffAvatar from './AppStaffAvatar.vue';

// refs
const full = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.DATE_FULL))
</script>

<template>
  <main class="w-full h-full">

    <div class="relative w-full h-auto mx-auto bg-white py-5 px-5 flex flex-col gap-16 shadow-lg shadow-slate-500/50 md:py-10 md:px-20 lg:w-10/12 xl:w-9/12">

        <div class="w-full flex flex-col gap-7">

            <!-- start of title -->
            <h1 class="text-slate-900 text-xl font-bold lg:text-4xl">This is the topic of the questionnaire</h1>
            <!-- end of title -->

            <!-- start of staff and date -->
            <div class="w-full flex items-center justify-between">
                <AppStaffAvatar />
            </div>
            <!-- end of staff and date -->


        </div>

    </div>
  </main>
</template>