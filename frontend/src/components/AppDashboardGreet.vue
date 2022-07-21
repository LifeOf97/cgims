<script setup>
/* eslint-disable */
import { computed } from "vue";
import {DateTime} from "luxon";

// props
const props = defineProps({
  person: {
    type: Object,
    default: {
        profile: {first_name: 'Firstname', last_name: 'Lastname', other_name: 'Othername'}
    }},
})

// computed
const greet = computed(() => {
  const time = DateTime.now().toLocaleString(DateTime.TIME_24_SIMPLE).slice(0,2)
  if (time < 12) return "morning"
  else if ((time >= 12) && (time < 18)) return "afternoon"
  else return "evening"
})

// methods
const otherName = () => {
  if (props.person.profile.other_name) {
    return `.${props.person.profile.other_name[0]}.`
  }
  return ""
}
</script>

<template>
    <div class="flex flex-col">
        <p class="text-slate-500 text-xs lg:text-lg">Good {{greet}}</p>
        <h3 class="text-slate-800 text-xl font-black md:text-3xl">{{person.profile.first_name}} {{otherName()}} {{person.profile.last_name}}</h3>
    </div>
</template>
