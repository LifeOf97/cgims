<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '../stores/user';
import chairsImg from '../assets/images/chairs2.jpg'
import AppLogo from '../components/AppLogo.vue';
import AppInputField from '../components/AppInputField.vue';
import AppPasswordField from '../components/AppPasswordField.vue';
import AppCheckBox from '../components/AppCheckBox.vue';
import AppButton from '../components/AppButton.vue';
import IconLongLeft from '../components/icons/IconLongLeft.vue';
import IconCheckAllBig from '../components/icons/IconCheckAllBig.vue';
import IconCloseBig from '../components/icons/IconCloseBig.vue';
import IconInfoCircleOutline from '../components/icons/IconInfoCircleOutline.vue';
import AppTippySignInDetails from '../components/AppTippySignInDetails.vue'

// stores
const userStore = useUserStore()

// refs
const username = ref(JSON.parse(localStorage.getItem("cgims_username")))
const password = ref('')
const rememberMe = ref(JSON.parse(localStorage.getItem("cgims_username")) ? true:false)

// methods
const signIn = () => {
    const userData = {
        username: username.value,
        password: password.value,
        rememberMe: rememberMe.value
    }
    userStore.signIn(userData)

    password.value = ""
}

// hooks
onMounted(() => {
  userStore.getMe()
})
</script>

<template>
    <main class="relative w-screen h-screen min-h-[44rem]">
        <div class="w-full h-full flex">

            <div class="relative flex-1 h-full bg-white flex items-center justify-center">
                <div class="w-10/12 mx-auto flex flex-col justify-center gap-10 md:w-5/12 lg:w-7/12">

                    <div class="flex flex-col items-start justify-center gap-2">
                        <AppLogo />
                        <div class="w-full flex items-center justify-between">
                            <p class="text-lg font-semibold text-slate-700 md:text-xl">Sign into your account</p>
                            <IconInfoCircleOutline
                                v-tippy="{content: AppTippySignInDetails, theme: 'dark', allowHTML: true, animation: 'scale', interactive: true}"
                                class="w-6 h-6 fill-slate-400 transition-all duration-200 cursor-help hover:fill-slate-900 focus:outline-none" />
                        </div>
                    </div>

                    <form @submit.prevent="signIn()" class="w-full flex flex-col gap-5">

                        <!-- start of if sign in error -->
                        <div v-if="userStore.userSignIn.error">
                            <p class="text-xs text-red-500 font-medium">{{userStore.userSignIn.error}}</p>
                        </div>
                        <!-- end of if sign in error -->

                        <AppInputField v-model="username" label="Staff ID" placeholder="STF1234" />
                        <AppPasswordField v-model="password" />
                        <div class="w-full flex items-center justify-between">
                            <AppCheckBox v-model="rememberMe" label="Remember me" />
                            <RouterLink to="#"
                                v-tippy="{ content: 'Not available', animation: 'scale', trigger: 'click' }"
                                class="text-blue-500 text-xs hover:text-blue-600">Forgot password?</RouterLink>
                        </div>
                        <AppButton :type="2" :color="2" :loading="userStore.userSignIn.loading" label="Sign In" class="mt-2" />
                    </form>

                </div>

                <!-- start of back to home link -->
                <div class="w-10/12 absolute top-0 flex items-center justify-end py-5 md:w-5/12 lg:w-7/12">
                    <div class="flex items-center gap-2 group">
                        <IconLongLeft class="w-7 h-7 fill-slate-300 group-hover:animate-bounce-left" />
                        <RouterLink :to="{ name: 'home' }" class="text-blue-500 text-xs font-medium md:text-sm">Home
                        </RouterLink>
                    </div>
                </div>
                <!-- end of back to home link -->

            </div>

            <div class="hidden relative flex-1 w-full lg:block">
                <img :src="chairsImg" alt="Image" class="h-full w-full object-cover">
                <div class="absolute bottom-4 right-4 flex gap-1 text-xs text-white font-medium">
                    <p>Photo by</p>
                    <a class="border-b border-rose-500 italic"
                        href="https://unsplash.com/@te3pot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Trung
                        Pham Quoc</a>
                    on
                    <a class="border-b border-rose-500 italic"
                        href="https://unsplash.com/@te3pot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
                </div>
            </div>
        </div>


        <!-- start of successful sign in notification -->
        <transition
            name="slide"
            enter-from-class="translate-y-20 opacity-0"
            enter-active-class="transition-all duration-200"
            leave-to-class="translate-y-20 opacity-0"
            leave-active-class="transition-all duration-700">
            <div v-if="userStore.userSignIn.success" class="w-full bg-transparent absolute top-10 flex items-center justify-center">
                <div class="bg-white flex items-center gap-5 px-4 py-2 shadow-lg shadow-slate-300 rounded-lg">
                    <div class="p-1 border border-green-500 flex items-center justify-center rounded-full">
                        <IconCheckAllBig class="w-3 h-3 fill-green-500" />
                    </div>
                    <p class="text-xs text-slate-900 font-medium">Signed in successfully</p>
                    <button type="button" @click="userStore.userSignIn.success = false">
                        <IconCloseBig class="w-5 h-5 fill-slate-400" />
                    </button>
                </div>
            </div>
        </transition>
        <!-- end of successful sign in notification -->
    </main>
</template>