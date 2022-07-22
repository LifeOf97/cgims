<script setup>
/* eslint-disable */

// props
const props = defineProps({
  person: {type: Object}
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
  <main class="flex items-center gap-3 group cursor-default">
    <button
      @click.prevent
      class="flex items-center justify-center h-8 w-8 cursor-default overflow-hidden ring-rose-600 ring-offset-2 ring-offset-white bg-rose-500 rounded-full transition-all duration-200 group-hover:ring-2">
        <img v-if="props.person.profile.image" :src="props.person.profile.image" alt="Image" class="w-full h-full object-cover object-center">
        <p v-else class="font-semibold text-lg text-white">{{props.person.profile.first_name[0]}}</p>
    </button>
    <div class="flex flex-col">
        <p class="text-sm text-slate-700 font-semibold max-w-[7rem] truncate">{{props.person.profile.first_name}} {{otherName()}} {{props.person.profile.last_name}}</p>
        <p class="text-xs text-slate-400 font-semibold uppercase">{{props.person.profile.username}}</p>
    </div>
  </main>
</template>
