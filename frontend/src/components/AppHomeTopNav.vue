<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import AppLogo from './AppLogo.vue'
import IconHamburger from './icons/IconHamburger.vue';
</script>

<template>
  <nav class="w-full">

    <div class="w-11/12 mx-auto flex justify-between items-center py-5 md:py-7 md:w-10/12 lg:w-9/12">

        <!-- start of logo -->
        <div>
            <AppLogo />
        </div>
        <!-- end f logo -->

        <!-- start of links for lrage screens -->
        <div class="hidden w-9/12 items-center justify-between md:flex">
            <div class="flex gap-7">
                <RouterLink :to="{name: 'home'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">About</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Why</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">How</RouterLink>
                <RouterLink :to="{name: 'home'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Contact Us</RouterLink>
            </div>
            <div class="flex items-center gap-5">
                <RouterLink :to="{name: 'home'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Staffs</RouterLink>
                <RouterLink :to="{name: 'home'}" class="bg-rose-500 px-4 py-1 text-sm text-white font-semibold rounded-md transition-all duration-200 hover:shadow-lg hover:scale-105">Students</RouterLink>
            </div>
        </div>
        <!-- end of links for lrage screens -->

        <!-- start of links for lrage screens -->
        <button type="button" @click.prevent class="md:hidden">
            <IconHamburger class="w-8 h-8 fill-slate-800 hover:fill-rose-500 transition-all duration-200" />
        </button>
        <!-- end of links for lrage screens -->
        

    </div>

  </nav>
</template>