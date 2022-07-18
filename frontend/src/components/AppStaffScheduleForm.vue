<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { DateTime } from "luxon"; 
import { DatePicker } from 'v-calendar';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconCalendar from './icons/IconCalendar.vue';

// refs
const expire = ref("")
const weekday = ref(DateTime.now().setLocale("en-US").toLocaleString({weekday: 'long'}))
const full = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.DATE_FULL))
const time = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.TIME_SIMPLE))
const minDate = ref(DateTime.now().plus({days: 1}).toISODate())
</script>

<template>
  <main class="w-full h-full">

    <form @submit.prevent class="w-full flex flex-col gap-7">

        <AppInputField label="Title" v-model="title" placeholder="Enter schedule title..." />

        <div class="w-full h-full flex flex-col gap-2">
            <label for="question" class="text-slate-700 text-xs font-medium md:text-sm">Detail</label>
            <textarea
                name="question"
                id="question"
                cols="30"
                rows="10"
                required
                placeholder="Enter schedule details..."
                class="w-full resize-none p-2 bg-slate-100 font-normal text-xs text-slate-900 rounded-sm ring-rose-500 ring-offset-2
                ring-offset-rose-100 shadow transition-all duration-200 hover:ring-2 focus:ring-2 focus:outline-none md:text-sm"></textarea>
        </div>

        <div class="flex items-center justify-end gap-5">
            <label for="expire" class="relative cursor-pointer group border">
                <input type="text" name="expire" id="expire" required class="absolute bg-transparent w-7 h-7 cursor-pointer">
                <DatePicker mode="date" v-model="expire" :min-date="minDate">
                    <template v-slot="{togglePopover}" class="relative">
                        <button @click.prevent="togglePopover()" class="relative">
                            <IconCalendar class="w-7 h-7 fill-slate-400 transition-all duration-200 group-hover:fill-slate-900" />
                        </button>
                    </template>
                </DatePicker>
            </label>

            <AppButton label="Create" :type="2" :color="2" />
        </div>

    </form>

  </main>
</template>