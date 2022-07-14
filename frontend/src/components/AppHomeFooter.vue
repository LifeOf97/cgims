<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import {gsap} from "gsap";
import {ScrollTrigger} from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// refs
const startAnim = ref(null)
const footTxt = ref(null)
const footTxt2 = ref(null)

// methods
const animFooter = () => {
    gsap.from(footTxt.value, {scrollTrigger: {trigger: startAnim.value, start: "100px bottom", markers: false, id: "footer"}, duration: 1.5, y: 50, opacity: 0,})
    gsap.from(footTxt2.value, {scrollTrigger: {trigger: startAnim.value, start: "100px bottom", markers: false, id: "footer"}, duration: 1.5, y: -50, opacity: 0,})
}

// hooks
onMounted(() => {
    animFooter()
})
</script>

<template>
  <main class="w-full bg-white">

    <div ref="startAnim" class="w-11/12 mx-auto flex flex-col pb-10 md:w-10/12 lg:w-9/12">
        <div ref="footTxt" class="flex flex-col gap-2">
            <p class="text-sm font-bold text-slate-500 md:text-base">Please Note</p>
            <div class="w-7/12 flex flex-col gap-5 md:w-4/12">
                <p class="text-xs italic font-normal text-slate-400">
                    All images, illustrations and explanations used by the developer
                    have been duly attributed to their respective owners and sources.
                </p>
            </div>
        </div>
    </div>

    <div class=" border-t border-slate-200 py-10">
        <div ref="footTxt2" class="w-11/12 mx-auto flex flex-col gap-2 items-center justify-between md:flex-row md:w-10/12 lg:w-9/12">

            <div class="flex gap-2 items-center text-xs text-slate-600">
                <p>Copyright &copy; 2022</p>
                <p>CGIMS</p>
            </div>

            <div class="flex gap-2 items-center text-xs text-slate-600">
                <p>Developed by the</p>
                <a
                    href="https://twitter.com/realestKMA"
                    target="_blank"
                    title="KMA = Kelvin Mayowa Ayeni"
                    class="text-blue-500 hover:text-blue-600">
                    RealestKMA
                </a>
                <p>from the</p>
                <p class="font-bold">234<flag iso="ng" /></p>
            </div>

        </div>

    </div>
    

  </main>
</template>