<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// refs
const startAnim = ref(null)
const footTxt = ref(null)
const footTxt2 = ref(null)

// methods
const animFooter = () => {
    gsap.from(footTxt.value, { scrollTrigger: { trigger: startAnim.value, start: "100px bottom", markers: false, id: "footer" }, duration: 1, y: 50, opacity: 0, })
    gsap.from(footTxt2.value, { scrollTrigger: { trigger: startAnim.value, start: "100px bottom", markers: false, id: "footer" }, duration: 1, y: -50, opacity: 0, })
}

// hooks
onMounted(() => {
    animFooter()
})
</script>

<template>
    <main class="w-full bg-white">

        <div class="flex flex-col gap-10 border-t border-slate-200 py-10">
            <div ref="footTxt2" class="w-11/12 mx-auto flex flex-col gap-2 items-center justify-between md:flex-row md:w-10/12 lg:w-9/12">

                <div class="flex gap-2 items-center text-xs text-slate-600">
                    <p>Copyright &copy; 2022</p>
                    <p>CGIMS</p>
                </div>

                <div class="flex gap-2 items-center text-xs text-slate-600">
                    <p>Developed by the</p>
                    <a href="https://twitter.com/realestKMA" target="_blank"
                        v-tippy="{ content: 'KMA = Kelvin Mayowa Ayeni', animation: 'scale' }"
                        class="text-blue-500 hover:text-blue-600">
                        RealestKMA
                    </a>
                    <p>from the</p>
                    <p class="font-bold">234
                        <flag iso="ng" />
                    </p>
                </div>

            </div>

            <div ref="startAnim" class="w-11/12 mx-auto flex flex-col md:w-10/12 lg:w-9/12">
                <div ref="footTxt" class="flex flex-col items-center gap-2 md:items-start">
                    <p class="text-xs font-normal text-slate-500 md:text-base">Please Note</p>
                    <div class="w-10/12 flex flex-col gap-5 md:w-5/12 lg:w-3/12">
                        <p class="text-xs text-center italic font-normal text-slate-400 md:text-left">
                            All images, illustrations and explanations from third party sources
                            used by the developer have been duly attributed to their respective
                            owners and/or sources. in cases where it is not obvious please hover
                            your mouse or touch on the respective content to see the attribution.
                        </p>
                    </div>
                </div>
            </div>

            <div class="flex items-center justify-center gap-2 text-xs w-11/12 mx-auto md:w-10/12 lg:w-9/12">
                <p class="font-medium text-slate-900">API Docs: </p>
                <a class="cursor-pointer text-blue-500 hover:text-blue-600" href="https://cgims.herokuapp.com/api/schema/swagger/" target="_blank" rel="noopener noreferrer">Swagger,</a>
                <a class="cursor-pointer text-blue-500 hover:text-blue-600" href="https://cgims.herokuapp.com/api/schema/redoc/" target="_blank" rel="noopener noreferrer">Redoc</a>
            </div>

        </div>


    </main>
</template>
