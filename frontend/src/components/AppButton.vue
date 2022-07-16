<script setup>
/* eslint-disable */
import IconLoading from "./icons/IconLoading.vue"

// props
const props = defineProps({
    label: {type: String, default: "Submit"},
    loading: {type: Boolean, default: false},
    bgColor: {type: String, default: 'rose'},
    textColor: {type: String, default: 'white'}
})
</script>

<template>
  <main class="w-full">
    <button
        type="submit"
        :disabled="loading"
        :class="[props.bgColor == 'white' ? 'bg-white hover:bg-slate-200':'bg-rose-500 hover:bg-rose-600',
        props.textColor == 'white' ? 'text-white':'text-slate-900']"
        class="w-full p-2 text-center text-sm rounded transition-all duration-200
        disabled:bg-rose-400 disabled:cursor-wait md:text-base">
        <div v-if="props.loading" class="w-full flex items-center justify-center">
            <IconLoading class="w-7 h-7 fill-white animate-spin" />
        </div>
        <p v-else class="font-medium text-sm md:text-base">{{props.label}}</p>
    </button>
  </main>
</template>
