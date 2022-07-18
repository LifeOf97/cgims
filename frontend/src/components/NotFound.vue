<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="w-11/12 mx-auto h-screen min-h-[44rem] bg-white">

        <div class="w-full h-full flex flex-col items-center justify-center lg:flex-row">

            <div class="flex flex-col items divide-slate-500 md:flex-row md:divide-x md:divide-y-0">
                <span class=" text-red-600 text-4xl font-black pb-2 md:pr-2 md:text-6xl">404</span>
                <div class="flex flex-col gap-2 pt-2 md:pl-2">
                    <span class="text-slate-900 text-xl md:text-2xl">Page not found</span>
                    <span class="text-slate-500 font-normal text-xs md:text-sm">Please make sure the URL in the address bar is correct and try again</span>

                    <div class="flex self-start mt-3">
                        <RouterLink :to="{name: 'home'}" class="bg-blue-500 font-medium text-white px-6 py-2 rounded-md hover:bg-blue-600">
                            Back home
                        </RouterLink>
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>