/* eslint-disable */
import { defineStore } from "pinia";

export const useStaffQuestionnaireStore = defineStore({
    id: "questionnaire",
    state: () => ({
        create: {open: false, loading: false},
        edit: {open: false, loading: false},
        view: {open: false, loading: false},
        delete: {open: false, loading: false},
      }),
    actions: {
        increment() {
            this.counter++;
        },
    },
})