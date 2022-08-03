/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useStaffQuestionnaireStore = defineStore({
    id: "questionnaire",
    state: () => ({
        create: {open: false, loading: false, error: null},
        update: {open: false, loading: false, error: null},
        view: {open: false, loading: false},
        retrieve: {data: JSON.parse(localStorage.getItem("cgims_questionnaires")), loading: false, open: false, error: null},
        predefined: {data: JSON.parse(localStorage.getItem("cgims_predefined_questionnaires")), loading: false, error: null},
        delete: {open: false, loading: false, error: null},
        focus: {data: {id: null, completed: false, question: null, slug: null, title: null, students: [], categories: []}},
      }),
    getters: {
        latestFourQuestionnaires: (state) => {
            return state.retrieve.data.slice(0, 4)
        }
    },
    actions: {
        async createQuestionnaire(data) {
            const userStore = useUserStore()
            this.create.loading = true
            this.create.error = null

            await axios.post("staffs/me/questionnaires/create/", data, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.create.open = false
                    this.create.loading = false
                    this.create.error = null

                    // refresh the questionnaires list
                    // this.getQuestionnaires()
                    const questionnaires = JSON.parse(localStorage.getItem("cgims_questionnaires"))
                    questionnaires.unshift(resp.data)
                    localStorage.setItem("cgims_questionnaires", JSON.stringify(questionnaires))
                    this.retrieve.data = JSON.parse(localStorage.getItem("cgims_questionnaires"))
                })
                .catch((err) => {
                    this.create.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.create.error = "An error occured, please try again."
                })
        },
        async updateQuestionnaire(data) {
            const userStore = useUserStore()
            this.update.loading = true
            this.update.error = null
            const id = this.focus.data.id

            await axios.put(`staffs/me/questionnaires/${id}/update/`, data, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.update.open = false
                    this.update.loading = false
                    this.update.error = null

                    // refresh the questionnaires list
                    this.getQuestionnaires()
                })
                .catch((err) => {
                    this.update.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.update.error = "An error occured, please try again."
                })
        },
        async getQuestionnaires() {
            this.$reset()
            const userStore = useUserStore()
            this.retrieve.loading = true

            await axios.get("staffs/me/questionnaires/", {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.retrieve.loading = false
                    this.retrieve.error = null
                    this.retrieve.data = resp.data
                    localStorage.setItem("cgims_questionnaires", JSON.stringify(resp.data))
                })
                .catch((err) => {
                    this.retrieve.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.retrieve.error = "An error occured, please try again."
                })
        },
        async deleteQuestionnaire() {
            const userStore = useUserStore()
            this.delete.loading = true
            this.delete.error = null
            const id = this.focus.data.id

            await axios.delete(`staffs/me/questionnaires/${id}/delete/`, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    // refresh the questionnaires list
                    // this.getQuestionnaires()
                    const questionnaires = JSON.parse(localStorage.getItem("cgims_questionnaires"))
                    questionnaires.splice(questionnaires.indexOf(questionnaires.find((que) => que.id == this.focus.data.id)), 1)
                    localStorage.setItem("cgims_questionnaires", JSON.stringify(questionnaires))
                    this.retrieve.data = JSON.parse(localStorage.getItem("cgims_questionnaires"))

                    this.$reset()
                })
                .catch((err) => {
                    this.delete.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else if (err.response.status == 404) this.getQuestionnaires()
                    else this.delete.error = "An error occured, please try again."
                })
        },
        async getPredefinedQuestionnaires() {
            const userStore = useUserStore()
            this.predefined.loading = true
            this.predefined.error = null

            await axios.get(`questions/`, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.predefined.loading = false
                    this.predefined.error = null
                    this.predefined.data = resp.data
                    localStorage.setItem("cgims_predefined_questionnaires", JSON.stringify(resp.data))
                })
                .catch((err) => {
                    this.predefined.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.predefined.error = "An error occured, please try again."
                })
        }
    },
})