<script setup>
/* eslint-disable */

// props
const props = defineProps({
    modelValue: {type: Boolean, default: false},
    label: {type: String, default: "toggle"},
    text: {type: String, default: "Completed"},
    placement: {type: String, default: "right"}
})

// emits
const emits = defineEmits(["update:modelValue"])
</script>

<template>
    <main>

        <label
            :for="props.label"
            :class="props.placement == 'right' ? 'flex-row':'', props.placement == 'left' ? 'flex-row':'', props.placement == 'top' ? 'flex-col':'',
            props.placement == 'bottom' ? 'flex-col':''" class="flex gap-2 items-center flex-wrap group">

            <p
                :class="props.placement == 'top' ? 'order-1':'', props.placement == 'bottom' ? 'order-2':'', props.placement == 'right' ? 'order-2':'',
                props.placement == 'left' ? 'order-1':''" class="flex-initial text-slate-400 text-xs font-medium cursor-pointer group-hover:text-slate-900">{{props.text}}</p>
            
            <div
                :class="props.modelValue ? 'bg-green-500':'bg-slate-200', props.placement == 'top' ? 'order-2':'', props.placement == 'bottom' ? 'order-1':'',
                props.placement == 'right' ? 'order-1':'', props.placement == 'left' ? 'order-2':''"
                class="relative flex items-center w-14 h-6 rounded-full shadow-inner cursor-pointer">
                
                <div :class="props.modelValue ? 'translate-x-[2.1rem]':'translate-x-px'" class="w-5 h-5 rounded-full bg-white shadow transition-all duration-200"></div>
            </div>
        </label>

        <input
            type="checkbox"
            :name="label"
            :id="label"
            :checked="modelValue"
            @change="$emit('update:modelValue', $event.target.checked)"
            class="hidden">

    </main>
</template>