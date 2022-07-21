<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useUserStore } from "../stores/user";
import AppLogo from './AppLogo.vue'
import IconHamburger from './icons/IconHamburger.vue';
import IconCloseBig from './icons/IconCloseBig.vue';
import gsap from 'gsap'

// stores
const userStore = useUserStore()

// refs
const root = ref(null)
const mobileNav = ref(false)
const nav = ref(null)

// computed
const isAuthenticated = computed(() => {
    return JSON.parse(localStorage.getItem("cgims_user"))
})

const getStaffId = computed(() => {
    return JSON.parse(localStorage.getItem("cgims_staffid"))
})

// methods
const animNav = () => {
    gsap.from(nav.value, {opacity: 0, duration: 1})
}

const closeMobileNav = (e) => {
    if (!root.value.contains(e.target)) {
        mobileNav.value = false;
    }

}

// hooks
onMounted(() => {
    animNav()
    document.addEventListener("click", closeMobileNav)
})

onUnmounted(() => {
    document.removeEventListener("click", closeMobileNav)
})
</script>

<template>
  <nav ref="root" class="realtive w-full bg-white">

    <div ref="nav" class="w-11/12 mx-auto flex justify-between items-center py-5 md:py-7 md:w-10/12 lg:w-9/12">

        <!-- start of logo -->
        <div>
            <AppLogo />
        </div>
        <!-- end f logo -->

        <!-- start of links for lrage screens -->
        <div class="hidden w-9/12 items-center justify-between sm:flex">
            <div class="flex gap-7">
                <RouterLink to="/#about" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">About</RouterLink>
                <RouterLink to="/#why" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Why</RouterLink>
                <RouterLink to="/#how" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">How</RouterLink>
            </div>
            <div>
                <div v-if="isAuthenticated" class="flex items-center gap-5">
                    <button type="button" @click.prevent="userStore.userSignOut.open = true" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Sign out</button>
                    <RouterLink :to="{name: 'staff', params: {staffId: getStaffId}}" class="bg-rose-500 px-4 py-1 text-sm text-white font-semibold rounded-md transition-all duration-200 hover:shadow-lg hover:scale-105">Dashboard</RouterLink>
                </div>
                <div v-else class="flex items-center gap-5">
                    <RouterLink :to="{name: 'signinstaff'}" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Staffs</RouterLink>
                    <RouterLink v-tippy="{content: 'Coming soon &#128584', trigger: 'click', animation: 'scale'}" to="/" class="bg-rose-500 px-4 py-1 text-sm text-white font-semibold rounded-md transition-all duration-200 hover:shadow-lg hover:scale-105">Students</RouterLink>
                </div>
            </div>
        </div>
        <!-- end of links for lrage screens -->

        <!-- start of links for lrage screens -->
        <button type="button" @click.prevent="mobileNav = true" class="sm:hidden">
            <IconHamburger class="w-8 h-8 fill-slate-800 hover:fill-rose-500 transition-all duration-200" />
        </button>

        <transition
            name="slide-down"
            enter-from-class="scale-0 opacity-0"
            enter-active-class="transition-all duration-200"
            leave-to-class="scale-0 opacity-0"
            leave-active-class="transition-all duration-200">
            <div v-if="mobileNav" class="absolute top-0 left-0 w-full h-96 bg-white/70 backdrop-blur-lg z-20 shadow-lg shadow-black/50">
                <div class="flex flex-col gap-10">
                    <div class="p-7 flex items-center justify-between border-b border-slate-200">
                        <AppLogo />
                        <button type="button" @click.prevent="mobileNav = false" class="p-2 flex items-center justify-center rounded-lg bg-transparent transition-all duration-200 group hover:bg-rose-500">
                            <IconCloseBig class="w-7 h-7 fill-slate-900 transition-all duration-200 group-hover:fill-white" />
                        </button>
                    </div>
                    <div class="flex flex-col px-7">
                        <RouterLink @click="mobileNav = false" to="/#about" class="bg-transparent p-2 text-slate-900 text-base font-normal rounded-md hover:bg-rose-500 hover:text-white ">About</RouterLink>
                        <RouterLink @click="mobileNav = false" to="/#why" class="bg-transparent p-2 text-slate-900 text-base font-normal rounded-md hover:bg-rose-500 hover:text-white ">Why</RouterLink>
                        <RouterLink @click="mobileNav = false" to="/#how" class="bg-transparent p-2 text-slate-900 text-base font-normal rounded-md hover:bg-rose-500 hover:text-white ">How</RouterLink>
                    </div>
                    <div>
                        <div v-if="isAuthenticated" class="flex px-7 items-center justify-center gap-5 border-t border-slate-200 pt-5">
                            <button type="button" @click.prevent="userStore.userSignOut.open = true" class="text-slate-900 text-sm font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Sign out</button>
                            <RouterLink @click="mobileNav = false" :to="{name: 'staff', params: {staffId: getStaffId}}" class="bg-rose-500 px-4 py-1 text-base text-white font-semibold rounded-md transition-all duration-200 hover:shadow-lg hover:scale-105">Dashboard</RouterLink>
                        </div>
                        <div v-else class="flex px-7 items-center justify-center gap-5 border-t border-slate-200 pt-5">
                            <RouterLink @click="mobileNav = false" :to="{name: 'signinstaff'}" class="text-slate-900 text-base font-normal border-b-2 border-transparent transition-all duration-200 hover:border-rose-500 md:text-base">Staffs</RouterLink>
                            <RouterLink v-tippy="{content: 'Coming soon &#128584', animation: 'scale'}" to="/" class="bg-rose-500 px-4 py-1 text-base text-white font-semibold rounded-md transition-all duration-200 hover:shadow-lg hover:scale-105">Students</RouterLink>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
        <!-- end of links for lrage screens -->
        

    </div>

  </nav>
</template>