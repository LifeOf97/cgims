<script setup>
/* eslint-disable */
</script>

<template>
  <main class="flex items-center gap-3 group cursor-pointer">
    <button
      @click.prevent
      class="flex items-center justify-center h-8 w-8 overflow-hidden ring-rose-600 ring-offset-2 ring-offset-white bg-rose-500 rounded-full transition-all duration-200 group-hover:ring-2">
        <p class="font-semibold text-lg text-white">S</p>
    </button>
    <div class="flex flex-col">
        <p class="text-xs text-slate-700 font-semibold max-w-[7rem] truncate">Staff full name</p>
        <p class="text-xs text-slate-400 font-semibold">Staff</p>
    </div>
  </main>
</template>
