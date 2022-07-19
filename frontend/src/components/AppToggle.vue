<script setup>
/* eslint-disable */

// props
const props = defineProps({
    modelValue: {type: Boolean, default: false},
    label: {type: String, default: "toggle"},
    text: {type: String, default: "Completed"},
    textPos: {type: String, default: "bottom"}
})

// emits
const emits = defineEmits(["update:modelValue"])
</script>

<template>
    <main>

        <label :for="label" class="flex flex-col">
            <div :class="[props.modelValue ? 'bg-green-500':'bg-slate-200', textPos == 'top' ? 'order-2':'order-1']" class="relative flex items-center w-14 h-6 rounded-full shadow-inner cursor-pointer">
                <div :class="props.modelValue ? 'translate-x-[2.1rem]':'translate-x-px'" class="w-5 h-5 rounded-full bg-white shadow transition-all duration-200"></div>
            </div>
            <p :class="props.textPos == 'top' ? 'order-1 mb-2':'order-2 mt-2'" class="flex-initial text-slate-400 text-xs font-medium cursor-pointer hover:text-slate-900">{{props.text}}</p>
        </label>

        <input type="checkbox" :name="label" :id="label" @change="$emit('update:modelValue', $event.target.checked)" class="hidden">

    </main>
</template>