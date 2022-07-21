<script setup>
/* eslint-disable */
const props = defineProps({
    modelValue: {type: Boolean},
    label: {type: String, default: "Checkbox"},
})

const emits = defineEmits(['update:modelValue'])
</script>

<template>
  <main>
    <label :for="props.name" class="flex items-start gap-2 cursor-pointer ">
        <input
            type="checkbox"
            :name="props.label"
            :id="props.label"
            :checked="modelValue" 
            @change="$emit('update:modelValue', $event.target.checked)"
            class="ring-2 ring-transparent ring-offset-1 accent-rose-500 transition-all duration-200 hover:ring-rose-500"
        />
        <p class="text-xs text-slate-500 font-normal">{{props.label}}</p>
    </label>
  </main>
</template>