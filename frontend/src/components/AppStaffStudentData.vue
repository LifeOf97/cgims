<script setup>
/* eslint-disable */
import classRoomImg from '../assets/images/classroom.jpg'
import IconUser from './icons/IconUser.vue';

// props
const props = defineProps({
    firstName: {type: String, default: "First"},
    lastName: {type: String, default: "Last"},
    otherName: {type: String, default: "Other"},
    mugshot: {type: String, default: ""},
    department: {type: String, default: "Department"},
    class: {type: String, default: "jss1"},
    regNo: {type: String, default: "1234"},
    address: {type: String, default: "Address"},
    parent: {type: String, default: "Parent Name"},
    phone: {type: String, default: "+234 8065035596"},
    about: {type: String, default: "About me"},
})

// datas
const data = {
  inlineStyles: {
    backgroundImage: `url(${classRoomImg})`,
  }
}
</script>

<template>
  <main class="w-full h-full">

    <div class="flex flex-col gap-10">
        
        <div class="relative w-full h-full">
            <!-- start of classromm image, only visible on large screens -->
            <div class="h-60 bg-cover bg-center bg-gradient-to-tr from-slate-400 to-transparent" :style="inlineStyles"></div>
            <!-- end of classroom image, only visible on large screens -->

            <!-- start of student images -->
            <div class="absolute top-40 left-20 w-full h-40 rounded-lg overflow-hidden md:w-40">
                <img v-if="props.mugshot" :src="props.mugshot" alt="Image" class="w-full h-full object-cover object-center">
                <IconUser v-else class="w-full h-full fill-slate-200" />
            </div>
            <!-- end of student images -->
        </div>

    </div>

  </main>
</template>