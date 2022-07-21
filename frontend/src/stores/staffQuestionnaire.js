/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";


export const useStaffQuestionnaireStore = defineStore({
    id: "questionnaire",
    state: () => ({
        create: {open: false, loading: false, error: null},
        update: {open: false, loading: false, error: null},
        view: {data: null, open: false, loading: false},
        retrieve: {data: JSON.parse(localStorage.getItem("cgims_questionnaires")), loading: false, open: false, error: null},
        delete: {open: false, loading: false, error: null},
      }),
    getters: {
        latestFourQuestionnaires: (state) => {
            return state.retrieve.data.slice(0, 4)
        }
    },
    actions: {
        async createQuestionnaire(data) {
            this.create.loading = true
            this.create.error = null

            await axios.post("staffs/me/questionnaires/create/", data, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.create.loading = false
                    this.create.error = null

                    // refresh the questionnaires list
                    this.getQuestionnaires()
                })
                .catch((err) => {
                    this.create.loading = false
                    this.create.error = "An error occured, please try again."
                    console.log(err.response)
                })
        },
        async updateQuestionnaire(data) {
            this.create.loading = true
            this.create.error = null

            await axios.put(`staffs/me/questionnaires/${data['id']}/update/`, data, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.update.loading = false
                    this.update.error = null

                    // refresh the questionnaires list
                    this.getQuestionnaires()
                })
                .catch((err) => {
                    this.update.loading = false
                    this.update.error = "An error occured, please try again."
                    console.log(err.response)
                })
        },
        async getQuestionnaires() {
            this.retrieve.loading = true

            await axios.get("staffs/me/questionnaires/", {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.retrieve.loading = false
                    this.retrieve.error = null
                    localStorage.setItem("cgims_questionnaires", JSON.stringify(resp.data))
                    this.retrieve.data = JSON.parse(localStorage.getItem("cgims_questionnaires"))
                })
                .catch((err) => {
                    this.retrieve.loading = false
                    this.retrieve.error = "An error occured"
                    console.log(err.response)
                })
        }
    },
})