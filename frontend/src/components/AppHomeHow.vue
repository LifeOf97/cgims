<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import profileStory from '../assets/svgs/Profile.svg'
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// refs
const startAnim = ref(null)
const howTxt = ref(null)
const howImg = ref(null)

// methods
const animHow = () => {
    gsap.from(howTxt.value, {scrollTrigger: {trigger: startAnim.value, start: "250px bottom", markers: false, id: "how"}, duration: 1, x: 100, opacity: 0,})
    gsap.from(howImg.value, {scrollTrigger: {trigger: startAnim.value, start: "250px bottom", markers: false, id: "how"}, duration: 1, x: -100, opacity: 0,})
}

// hooks
onMounted(() => {
    animHow()
})
</script>

<template>
  <main id="how" class="w-full h-full bg-white selection:bg-blue-600 selection:text-white">

    <div class="w-11/12 py-10 mx-auto flex flex-col gap-5 md:w-10/12 lg:py-24 lg:w-9/12">

        <div ref="startAnim" class="w-full h-full flex flex-col gap-y-10 items-center lg:flex-row">

            <div ref="howTxt" class="flex-1 flex flex-col gap-4 lg:pr-10">
                <p class="self-start bg-blue-600 px-4 py-1 text-white text-xs font-medium rounded-full md:text-sm">How CGIMS</p>
                <h3 class="text-slate-900 text-2xl font-black md:text-3xl">How Career Guidance Information and Management System Works?</h3>
                <p class="text-xs text-slate-600 md:text-sm">
                    Web-based career guidance information and management system, creates the awareness to the use of computers in counselling.
                    This will provide a lasting solution to the problems affecting counselling exercise in secondary schools in Nigeria. The new
                    system will provide a technology-based, individually-operated platform that promotes interactivity with the students.<br><br>

                    Version 1 of the new system will provide questionnaires carefully crafted by the counselling office of the school in question,
                    in respect to the counselling guidelines by relevant educational, social and cultural authorities in the country. This will
                    then be used to engage with the students so as to collect answers from them.<br><br>
                    
                    Observations based on the answered questionnaires, a one on one counselling (if required) and an overall academic performace of
                    the students will be taken and stored in a relational database management system.<br><br>

                    This solution provides a secure RESTFUL API approach that can be easily utilized in whatever system the school in question
                    decides to develop in the future that needs the overall students personal data, observations from counselling staffs and more.
                </p>
            </div>

            <!-- start of story svg -->
            <div ref="howImg" class="relative flex-1 w-full">
                <img :src="profileStory" alt="Question Story" class="w-full h-full">
                <a href="https://storyset.com/people" target="_blank" class="absolute bottom-12 right-16 text-xs italic hover:text-blue-600 md:bottom-16">People illustrations by Storyset</a>
            </div>
            <!-- end of story svg -->

        </div>

    </div>

  </main>
</template>