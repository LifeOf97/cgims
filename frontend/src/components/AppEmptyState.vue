<script setup>
/* eslint-disable */
import IconInfoCircleOutline from './icons/IconInfoCircleOutline.vue';
</script>

<template>
  <main class="w-full h-full">

    <div
      class="w-full h-full p-10 flex flex-col items-center justify-center gap-4 border-2 border-dashed border-slate-200 bg-slate-50 rounded-lg md:p-20">
      <slot name="icon">
        <IconInfoCircleOutline class="w-16 h-16 fill-slate-300" />
      </slot>

      <div class="flex flex-col">
        <slot name="title">
          <p class="text-slate-500 text-xs font-normal text-center md:text-sm">
            This is the default empty state
          </p>
        </slot>
        <slot name="tail">
          <p class="text-slate-400 text-xs font-light text-center md:text-sm">
            They are powered by slots, so be free to insert anything.
          </p>
        </slot>
      </div>
    </div>

  </main>
</template>