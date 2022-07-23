<script setup>
/* eslint-disable */
import { Calendar } from 'v-calendar';
import {DateTime} from "luxon";

// props
const props = defineProps({
  attr: {type: Array, default: [{key: 'today', highlight: 'red', dates: new Date()}]}
})

// datas
const weekday = DateTime.now().setZone('Africa/Lagos').setLocale("en-US").toLocaleString({weekday: 'long'})
const fullDate = DateTime.now().setZone('Africa/Lagos').setLocale("en-US").toLocaleString(DateTime.DATE_FULL)

const attr = [
    {key: 'today', highlight: 'red', dates: new Date()}
]

// methods
const toDay = () => {

    return DateTime.now().setZone('Africa/Lagos')
}
</script>

<template>
  <main class="w-full h-full flex flex-col gap-10">
    <div class="flex flex-col gap-2">
        <p class="text-xs text-slate-500 font-medium md:text-lg">{{weekday}}</p>
        <p class="text-lg text-slate-900 font-semibold md:text-2xl">{{fullDate}}</p>
    </div>

    <Calendar :attributes="props.attr" is-expanded />
  </main>
</template>