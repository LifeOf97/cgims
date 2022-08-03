/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useStudentStore = defineStore({
    id: "student",
    state: () => ({
        retrieve: {data: JSON.parse(localStorage.getItem("cgims_students")), loading: false, error: null},
        focus: {data: null, loading: false, error: null}
    }),
    actions: {
        async getStudents() {
            const userStore = useUserStore()
            this.retrieve.loading = true
            this.retrieve.error = null

            await axios.get('students/', {headers: { 'Authorization': `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
                .then((resp) => {
                    this.retrieve.loading = false
                    this.retrieve.error = null
                    this.retrieve.data = resp.data
                    localStorage.setItem("cgims_students", JSON.stringify(resp.data))
                })
                .catch((err) => {
                    this.retrieve.loading = false
                    if (err.response.status == 401) userStore.signOut()
                    else this.create.error = "An error occured, please try again."
                })
        }
    }
})