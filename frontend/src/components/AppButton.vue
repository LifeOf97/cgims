<script setup>
/* eslint-disable */
import IconLoading from "./icons/IconLoading.vue"

// props
const props = defineProps({
    label: {type: String, default: "Submit"},
    loading: {type: Boolean, default: false},
    type: {type: Number, default: 1},
    color: {type: Number, default: 1},
})
</script>

<template>
  <main class="">

    <!-- start of button 1 -->
    <button
      v-if="props.type == 1"
      type="submit"
      :disabled="loading"
      :class="props.color == 1 ? 'bg-transparent border-slate-400 hover:border-slate-900 disabled:border-slate-200':'border-rose-500 hover:border-rose-600 disabled:border-rose-200'"
      class="group w-full px-4 py-2 text-center text-sm rounded border transition-all duration-200 hover:border-slate-900 disabled:border-slate-300 disabled:cursor-wait md:text-base">
      <div v-if="props.loading" class="w-full flex items-center justify-center">
          <IconLoading :class="props.textColor == 'white' ? 'fill-white':'fill-slate-900 group-disabled:fill-slate-400'" class="w-7 h-7 animate-spin" />
      </div>
      <p v-else :class="props.textColor == 'white' ? 'text-white':'text-slate-600 group-hover:text-slate-900'" class="font-medium text-xs transition-all duration-200 md:text-sm">{{props.label}}</p>
    </button>
    <!-- end of button 1 -->

    <!-- start of button 2 -->
    <button
      v-if="props.type == 2"
      type="submit"
      :disabled="loading"
      :class="props.color == 1 ? 'bg-white hover:bg-slate-400 disabled:bg-slate-200':'',
      props.color == 2 ? 'bg-rose-500 hover:bg-rose-600 disabled:bg-rose-400':'',
      props.color == 3 ? 'bg-slate-400 hover:bg-slate-500 disabled:bg-slate-300':''"
      class="group w-full px-4 py-2 text-center text-sm rounded transition-all duration-200 shadow-lg disabled:cursor-wait md:text-base">
      <div v-if="props.loading" class="w-full flex items-center justify-center">
          <IconLoading class="w-7 h-7 fill-white animate-spin" />
      </div>
      <p  v-else :class="props.color == 1 ? 'text-slate-900 group-hover:text-white':'text-white'" class="font-medium text-xs transition-all duration-200 md:text-sm">{{props.label}}</p>
    </button>
    <!-- end of button 2 -->

  </main>
</template>
