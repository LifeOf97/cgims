<script setup>
/* eslint-disable */
import { ref, onMounted } from "vue"
import studentsImg from '../assets/images/students.jpg'
import nigeriaImg from '../assets/images/Nigeria.png'
import waecImg from '../assets/images/waec.png'
import necoImg from '../assets/images/neco.png'
import jambImg from '../assets/images/jamb.png'
import gsap from "gsap"

// refs
const heroTag = ref(null)
const heroTxt = ref(null)
const heroTxt2 = ref(null)

// document classes
const heroImg = document.getElementsByClassName('heroImg')

// data
const data = {
  inlineStyles: {
    backgroundImage: `url(${studentsImg})`,
  }
}

// methods
const animHero = () => {
  gsap.from([heroTxt.value, heroTxt2.value], {y: 50, opacity: 0, stagger: 0.2, duration: 1, delay: 1})
  gsap.from(heroImg, {x: 50, opacity: 0, stagger: 0.2, duration: 0.5, delay: 2})
  gsap.from(heroTag.value, {y: -50, opacity: 0, duration: 1, delay: 3})
}

// hooks
onMounted(() => {
  animHero()
})
</script>

<template>
  <main class="relative w-full h-full min-h-full bg-cover bg-no-repeat bg-center" :style="data.inlineStyles">
    
    <div class="w-full h-full bg-gradient-to-r from-slate-100 via-slate-100/70 to-transparent pt-48 pb-32">

      <div class="w-11/12 mx-auto md:w-10/12 lg:w-9/12">

        <div class="flex flex-col">

          <div ref="heroTag" class="max-w-full self-start bg-slate-300 text-xs flex items-center gap-3 rounded-full p-1 shadow-inner shadow-slate-400">
            <p class="bg-rose-500 text-white tracking-widest rounded-full font-medium px-2 py-1">CGIMS</p>
            <p class="font-semibold text-slate-700 pr-1 truncate">Career Guidance Information and Management System</p>
          </div>

          <div ref="heroTxt" class="text-3xl font-black mt-7 mb-2 md:text-4xl lg:text-5xl">
            <p class="leading-tight">Help The Younger One’s</p>
            <p>Decide Their <span class="text-rose-500">Career</span> Path</p>
          </div>

          <div ref="heroTxt2">
            <p class="w-11/12 text-slate-600 text-xs font-normal md:text-sm md:w-7/12 lg:w-5/12">
              As teachers, parents and guardians, children look up to us
              for direction. We should not outrightly decide their path,
              but help them in deciding their career path.
            </p>
          </div>

          <div class="flex gap-5 mt-5 md:mt-10 md:gap-10">
            <img :src="nigeriaImg" alt="Nigeria" title="nigeria map logo" class="heroImg w-7 h-7 md:w-10 md:h-10">
            <img :src="waecImg" alt="WAEC" title="waec logo" class="heroImg w-7 h-7 md:w-10 md:h-10">
            <img :src="necoImg" alt="NECO" title="neco logo" class="heroImg w-7 h-7 md:w-10 md:h-10">
            <img :src="jambImg" alt="JAMB" title="jamb logo" class="heroImg w-7 h-7 md:w-10 md:h-10">
          </div>
        </div>
      </div>
    </div>

    <div class="absolute bottom-4 right-4 flex gap-1 text-xs text-white font-medium">
      <p>Photo by</p>
      <a class="border-b border-rose-500 italic" href="https://unsplash.com/@benwhitephotography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ben White</a>
      on
      <a class="border-b border-rose-500 italic" href="https://unsplash.com/s/photos/school-children-in-haiti?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    </div>

  </main>
</template>