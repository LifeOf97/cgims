<script setup>
/* eslint-disable */
import classRoomImg from '../assets/images/classroom.jpg'
import IconUser from './icons/IconUser.vue';
import IconLongLeft from './icons/IconLongLeft.vue';

// props
const props = defineProps({
  firstName: { type: String, default: "First" },
  lastName: { type: String, default: "Last" },
  otherName: { type: String, default: "Other" },
  mugshot: { type: String, default: "" },
  department: { type: String, default: "Department" },
  class: { type: String, default: "jss1" },
  regNo: { type: String, default: "1234" },
  address: { type: String, default: "Address" },
  parent: { type: String, default: "Parent Name" },
  phone: { type: String, default: "+234 8065035596" },
  about: { type: String, default: "About me" },
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

    <div class="flex flex-col gap-10 py-10">

      <div class="relative w-full h-full">
        <!-- start of classromm image, only visible on large screens -->
        <div class="relative hidden overflow-hidden rounded-md md:block md:h-60">
          <div class="w-full h-full bg-cover bg-center" :style="data.inlineStyles"></div>
          <div class="absolute top-0 h-full w-full bg-gradient-to-r from-slate-400 to-transparent"></div>

          <!-- start of photo credit -->
          <div class="absolute bottom-4 right-4 flex gap-1 text-xs text-white font-medium">
            <p>Photo by</p>
            <a class="border-b border-rose-500 italic" href="https://unsplash.com/@bisworaj?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bisworaj Saheb</a>
            on
            <a class="border-b border-rose-500 italic" href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
          </div>
          <!-- start of photo credit -->

        </div>
        <!-- end of classroom image, only visible on large screens -->

        <!-- start of student images -->
        <div
          class="w-full h-60 bg-slate-200 rounded-lg overflow-hidden md:absolute top-36 md:h-40 md:w-40 md:left-10">
          <img v-if="props.mugshot" :src="props.mugshot" alt="Image" class="w-full h-full object-cover object-center">
          <IconUser v-else class="w-full h-full fill-slate-400" />
        </div>
        <!-- end of student images -->

        <div class="w-full h-full mt-16 pb-10 md:mt-28 xl:w-10/12">
          <div class="w-full h-full grid gap-7 grid-cols-1 sm:grid-cols-2 lg:gap-10 xl:grid-cols-3">

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">First Name</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.firstName }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Last Name</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.lastName }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Other Name</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.otherName }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Department</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.department }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Class</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.class }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Reg No</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.regNo }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Address</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.address }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Parent</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.parent }}</p>
            </span>

            <span class="flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">Contact</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.phone }}</p>
            </span>

            <span class="col-span-full flex flex-col gap-1">
              <p class="text-xs text-slate-500 font-normal">About Me</p>
              <p class="text-xs text-slate-900 font-semibold md:text-sm">{{ props.about }}</p>
            </span>
          </div>
        </div>

        <div class="flex items-center justify-start border-t border-slate-200 pt-5">
          <div class="flex items-center gap-2 group">
            <IconLongLeft class="w-7 h-7 fill-slate-300 group-hover:animate-bounce-left" />
            <RouterLink :to="{ name: 'staffstudents' }" class="text-blue-500 text-xs font-medium md:text-sm">Go back
            </RouterLink>
          </div>
        </div>
      </div>

    </div>

  </main>
</template>