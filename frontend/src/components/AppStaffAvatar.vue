<script setup>
/* eslint-disable */

// props
const props = defineProps({
  firstName: {type: String, default: "First"},
  lastName: {type: String, default: "Last"},
  otherName: {type: String, default: "Other"},
  staffId: {type: String, default: "STF1234"},
  mugshot: {type: String, default: ""},
})

// methods
const fullName = () => {
  return `${props.firstName} .${props.otherName[0]}. ${props.lastName}`
}
</script>

<template>
  <main class="flex items-center gap-3 group cursor-pointer">
    <button
      @click.prevent
      class="flex items-center justify-center h-8 w-8 overflow-hidden ring-rose-600 ring-offset-2 ring-offset-white bg-rose-500 rounded-full transition-all duration-200 group-hover:ring-2">
        <img v-if="props.mugshot" :src="mugshot" alt="Image" class="w-full h-full object-cover object-center">
        <p v-else class="font-semibold text-lg text-white">{{props.firstName[0]}}</p>
    </button>
    <div class="flex flex-col">
        <p class="text-sm text-slate-700 font-semibold max-w-[7rem] truncate">{{fullName()}}</p>
        <p class="text-xs text-slate-400 font-semibold">{{props.staffId}}</p>
    </div>
  </main>
</template>
