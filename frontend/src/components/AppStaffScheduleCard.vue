<script setup>
/* eslint-disable */
import { ref, watch } from "vue";
import {DateTime} from "luxon";
import AppButton from "./AppButton.vue";
import AppToggle from "./AppToggle.vue";
import IconFlag from './icons/IconFlag.vue'

// props
const props = defineProps({
    schedule: {type: Object, default: {completed: false, title: 'Title', detail: "Detail"}}
})
const completed = ref(props.schedule.completed)
const update = ref(false)

// methods
const displayDate = (value) => {
    return DateTime.fromISO(value).setLocale("en-US").toLocaleString(DateTime.DATETIME_MED);
}

// watchers
watch(completed, (newValue, oldValue) => {
    if (completed.value === newVal) update.value = true
    else update.value = false
})
</script>

<template>
    <main>

        <details class="flex flex-col gap-4 bg-slate-100 rounded-md p-4 shadow transition-all duration-500 open:shadow-lg hover:shadow-lg">
            <summary class="flex items-center gap-4 cursor-pointer">
                <IconFlag class="w-7 h-7 fill-rose-500" />

                <span class="flex flex-col max-w-[80%]">
                    <p class="text-sm text-slate-700 font-medium truncate md:text-base">{{props.schedule.title}}</p>
                    <p class="text-xs text-slate-500 font-light md:text-sm">created: {{displayDate(props.schedule.created)}} </p>
                </span>
            </summary>

            <span class="flex flex-col gap-8 mt-4 ml-10">
                <p class="text-slate-500 text-sm font-normal">{{props.schedule.detail}}</p>

                <!-- buttons -->
                <div class="flex items-center justify-between border-t pt-2">
                    <AppToggle v-model="props.schedule.completed" :label="props.schedule.title" text="Completed" />
                    <div class="flex gap-3">
                        <AppButton label="Update" :type="1" :color="1" />
                        <AppButton  label="Delete" :type="2" :color="2" />
                    </div>
                </div>
            </span>

        </details>
        
    </main>
</template>