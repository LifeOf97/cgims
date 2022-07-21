<script setup>
/* eslint-disable */
import { useUserStore } from './stores/user';
import AppNotificationModal from './components/AppNotificationModal.vue';
import AppButton from './components/AppButton.vue';
import IconLogOut from './components/icons/IconLogOut.vue';

// stores
const userStore = useUserStore()
</script>

<template>
  <div class="w-full h-full min-h-full bg-white font-Poppins select-text overflow-hidden selection:text-white selection:bg-rose-500">
    <RouterView />

    <teleport to="#app">
      <transition
        name="scale"
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-200"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-200">
          <div v-if="userStore.userSignOut.open" class="fixed w-full h-full z-50 flex items-end justify-center bg-slate-400/50 backdrop-blur-lg overflow-auto md:items-center">
            <AppNotificationModal>
              <template #icon><IconLogOut class="w-7 h-7 fill-rose-500" /></template>
              <template #header>Sign Out</template>
              <template #detail>Are you sure you want to sign out?</template>
              <template #buttons>
                <AppButton class="w-full md:w-auto" @click.prevent="userStore.userSignOut.open = false" label="Cancle" :type="1" :color="1" />
                <AppButton class="w-full md:w-auto" @click.prevent="userStore.signOut()" label="Sign out" :type="2" :color="2" />
              </template>
            </AppNotificationModal>
          </div>
      </transition>
    </teleport>
  </div>
</template>
