<script setup>
/* eslint-disable */
const props = defineProps({
  modelValue: {type: String},
  label: {type: String, default: "Text"},
  type: {type: String, default: "text"},
  required: {type: Boolean, default: true},
  placeholder: {type: String, default: "Enter value..."},
  maxLength: {type: Number, default: 100}
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <div class="flex flex-col gap-1">

    <label :for="label" class="text-slate-700 text-xs font-medium md:text-sm">
      {{ props.label }}
    </label>

    <input
      :value="props.modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :type="type"
      :name="props.label"
      :id="props.label"
      :maxlength="maxLength"
      :placeholder="placeholder"
      :required="required"
      class="w-full p-2 bg-slate-100 font-normal text-xs text-slate-900 rounded-sm ring-rose-500 ring-offset-2
      ring-offset-rose-100 shadow transition-all duration-200 hover:ring-2 focus:ring-2 focus:outline-none md:text-sm
      "
    />

  </div>
</template>