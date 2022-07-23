<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useStaffScheduleStore } from '../stores/staffSchedule';
import { DateTime } from "luxon"; 
import { DatePicker } from 'v-calendar';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';
import IconCalendar from './icons/IconCalendar.vue';

// refs
const title = ref("")
const detail = ref("")
const expire = ref("")
const weekday = ref(DateTime.now().setLocale("en-US").toLocaleString({weekday: 'long'}))
const full = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.DATE_FULL))
const time = ref(DateTime.now().setLocale("en-US").toLocaleString(DateTime.TIME_SIMPLE))
const minDate = ref(DateTime.now().plus({days: 1}).toISODate())

// stores
const scheduleStore = useStaffScheduleStore()

// methods
const formatDate = () => {
    const date = DateTime.fromJSDate(expire.value)
    if (expire.value) return date.setLocale("en-US").toISODate(DateTime.DATE_FULL)
    else return "";
}

const submit = () => {
    const data = {
        title: title.value,
        detail: detail.value,
        expire: formatDate()
    }
    scheduleStore.createSchedule(data)

}

// vue calendar
const selectAttribute = {
    highlight: 'red'
}
</script>

<template>
  <main class="w-full h-full flex flex-col gap-7">

    <div class="border-b border-slate-200 pb-2">
        <h3 class="text-lg text-slate-900 font-semibold tracking-wider md:text-2xl">Create a schedule</h3>
    </div>

    <form @submit.prevent="submit()" class="w-full flex flex-col gap-7">

        <AppInputField label="Title" v-model="title" placeholder="Enter schedule title..." />

        <div class="w-full h-full flex flex-col gap-2">
            <label for="question" class="text-slate-700 text-xs font-medium md:text-sm">Detail</label>
            <textarea
                name="question"
                id="question"
                cols="30"
                rows="10"
                required
                v-model="detail"
                placeholder="Enter schedule details..."
                class="w-full resize-none p-2 bg-slate-100 font-normal text-xs text-slate-900 rounded-sm ring-rose-500 ring-offset-2
                ring-offset-rose-100 shadow transition-all duration-200 hover:ring-2 focus:ring-2 focus:outline-none md:text-sm"></textarea>
        </div>

        <div class="flex items-center justify-end gap-3">
            <!-- start of error detail -->
            <ul v-if="scheduleStore.create.error">
                <li class="list-disc list-inside text-red-500 text-xs font-normal">{{scheduleStore.create.error}}</li>
            </ul>
            <!-- end of error detail -->

            <div class="flex items-center gap-2">
                <div class="text-xs text-slate-900 font-medium flex items-center gap-2">
                    <p>Expires:</p>
                    <p :class="formatDate() ? 'px-4 py-2':''" class="text-xs text-slate-700 font-medium rounded-lg bg-slate-200 shadow-inner shadow-slate-400">{{formatDate()}}</p>
                </div>
                <label for="expire" class="relative cursor-pointer group mt-2">
                    <input v-model="expire" type="text" name="expire" id="expire" required class="absolute bg-transparent w-7 h-7 cursor-pointer text-transparent -z-0 focus:outline-none">
                    <DatePicker mode="date" v-model="expire" :min-date="minDate" :select-attribute="selectAttribute">
                        <template v-slot="{togglePopover}" class="relative">
                            <button @click.prevent="togglePopover()" class="relative">
                                <IconCalendar class="w-7 h-7 fill-slate-500 transition-all duration-200 group-hover:fill-slate-900" />
                            </button>
                        </template>
                    </DatePicker>
                </label>
                <AppButton label="Create" :type="2" :color="2" :loading="scheduleStore.create.loading" />
            </div>
        
        </div>

    </form>

  </main>
</template>