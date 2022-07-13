<script setup>
/* eslint-disable */
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="font-black text-lg md:text-xl">
    <RouterLink :to="{name: 'home'}">
      <h1 class="text-rose-500 leading-3">CAREER</h1>
      <h1 class="text-slate-900">GUIDANCE</h1>
    </RouterLink>
  </div>
</template>