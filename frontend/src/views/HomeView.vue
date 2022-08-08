<script setup>
/* eslint-disable */
import { onMounted } from 'vue';
import { useUserStore } from '../stores/user';
import AppHomeTopNav from '../components/AppHomeTopNav.vue';
import AppHomeHero from '../components/AppHomeHero.vue';
import AppHomeAbout from '../components/AppHomeAbout.vue';
import AppHomeWhy from '../components/AppHomeWhy.vue';
import AppHomeHow from '../components/AppHomeHow.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';

// stores
const userStore = useUserStore()

// hooks
onMounted(() => {
  userStore.wakeDyno()
})
</script>

<template>
  <main class="w-full h-full min-h-full">
    <div class="relative w-full h-full">

        <!-- start of top nav -->
        <nav>
          <AppHomeTopNav class="w-full" />
        </nav>
        <!-- end of top nav -->

        <!-- start of hero -->
        <header>
          <AppHomeHero />
        </header>
        <!-- end of hero -->

        <!-- start about of section -->
        <section>
          <AppHomeAbout />
        </section>
        <!-- end about of section -->

        <!-- start of why section -->
        <section>
          <AppHomeWhy />
        </section>
        <!-- start of why section -->

        <!-- start of how section -->
        <section>
          <AppHomeHow />
        </section>
        <!-- start of how section -->

        <!-- start of how section -->
        <footer>
          <AppHomeFooter />
        </footer>
        <!-- start of how section -->

    </div>
  </main>
</template>
