<script setup>
/* eslint-disable */
import IconWarningOutline from './icons/IconWarningOutline.vue'
import AppButton from './AppButton.vue';
</script>

<template>
  <main class="w-full h-auto overflow-hidden shadow-lg shadow-slate-500 md:rounded-lg md:w-96">

    <div class="flex flex-col">

        <div class="flex items-center gap-5 p-5 bg-white">
            <div class="self-start">
                <slot name="icon"><IconWarningOutline class="w-7 h-7 fill-rose-500" /></slot>
            </div>

            <div class="flex flex-col gap-3">
                <div class="text-base text-slate-900 font-bold md:text-lg">
                    <slot name="header">Notification Header</slot>
                </div>
                <div class="text-xs text-slate-500 font-normal md:text-sm">
                    <slot name="detail">Notification details</slot>
                </div>
            </div>
        </div>

        <div class="flex flex-col items-center justify-end gap-2 p-3 bg-slate-100 md:flex-row">
            <slot name="buttons">
                <AppButton class="w-full md:w-auto" label="No" :type="1" :color="1" />
                <AppButton class="w-full md:w-auto" label="Yes" :type="2" :color="2" />
            </slot>
        </div>
    </div>

  </main>
</template>
