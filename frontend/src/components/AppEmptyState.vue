<script setup>
/* eslint-disable */
</script>

<template>
  <main class="w-full h-full">

    <div class="w-full h-full p-10 flex flex-col items-center justify-center gap-4 border-2 border-dashed border-slate-200 bg-slate-50 rounded-lg md:p-20">
        <slot name="icon"></slot>

        <div class="flex flex-col">
            <slot name="title"></slot>
            <slot name="tail"></slot>
        </div>
    </div>

  </main>
</template>