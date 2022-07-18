<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import chairsImg from '../assets/images/chairs2.jpg'
import AppLogo from '../components/AppLogo.vue';
import AppInputField from '../components/AppInputField.vue';
import AppPasswordField from '../components/AppPasswordField.vue';
import AppCheckBox from '../components/AppCheckBox.vue';
import AppButton from '../components/AppButton.vue';
import IconLongLeft from '../components/icons/IconLongLeft.vue';

// refs
const rememberMe = ref(false)
const password = ref('')
const loading = ref(false)
</script>

<template>
  <main class="w-screen h-screen min-h-[44rem]">
    <div class="w-full h-full flex">
        
        <div class="relative flex-1 h-full bg-white flex items-center justify-center">
            <div class="w-10/12 mx-auto flex flex-col justify-center gap-10 md:w-5/12 lg:w-7/12">

                <div class="flex flex-col items-center justify-center gap-2 lg:items-start">
                    <AppLogo />
                    <p class="text-lg font-semibold text-slate-700 md:text-xl">Sign into your account</p>
                </div>

                <form @submit.prevent="loading = !loading" class="w-full flex flex-col gap-5">
                    <AppInputField label="Staff ID" placeholder="STF1234" />
                    <AppPasswordField v-model="password" />
                    <div class="w-full flex items-center justify-between">
                        <AppCheckBox v-model="rememberMe" label="Remember me" />
                        <RouterLink to="#" v-tippy="{content: 'Coming soon', animation: 'scale', trigger: 'click'}" class="text-blue-500 text-xs hover:text-blue-600">Forgot password?</RouterLink>
                    </div>
                    <AppButton type="2" :loading="loading" label="Sign In" class="mt-2" />
                </form>

            </div>
            
            <!-- start of back to home link -->
            <div class="w-10/12 absolute top-0 flex items-center justify-end py-5 md:w-5/12 lg:w-7/12">
                <div class="flex items-center gap-2 group">
                    <IconLongLeft class="w-7 h-7 fill-slate-300 group-hover:animate-bounce-left" />
                    <RouterLink :to="{name: 'home'}" class="text-blue-500 text-xs font-medium md:text-sm">Home</RouterLink>
                </div>
            </div>
            <!-- end of back to home link -->
        </div>

        <div class="hidden relative flex-1 w-full lg:block">
            <img :src="chairsImg" alt="Image" class="h-full w-full object-cover">
            <div class="absolute bottom-4 right-4 flex gap-1 text-xs text-white font-medium">
                <p>Photo by</p>
                <a class="border-b border-rose-500 italic" href="https://unsplash.com/@te3pot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Trung Pham Quoc</a>
                on
                <a class="border-b border-rose-500 italic" href="https://unsplash.com/@te3pot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
            </div>
        </div>
    </div>
  </main>
</template>