/* eslint-disable */
import { defineStore } from "pinia";

export const useStaffScheduleStore = defineStore({
    id: "schedule",
    state: () => ({
        delete: {open: false, loading: false},
      })
})