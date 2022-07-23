/* eslint-disable */
import { defineStore } from "pinia";
import { useUserStore } from "./user";
import axios from "axios";


export const useStaffScheduleStore = defineStore({
    id: "schedule",
    state: () => ({
        create: {loading: false, success: null, error: null},
        retrieve: { data: JSON.parse(localStorage.getItem("cgims_schedules")), loading: false, error: null},
        delete: {open: false, loading: false, id: null},
      }),
      actions: {
        async createSchedule(data) {
          const userStore = useUserStore()
          this.create.loading = true
          this.create.success = null
          this.create.error = null

          await axios.post("staffs/me/schedules/create/", data, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
            .then((resp) => {
              this.create.loading = false
              this.create.success = "Schedule created successfully"
              this.create.error = null

              const schedules = JSON.parse(localStorage.getItem("cgims_schedules"))
              schedules.push(resp.data)
              localStorage.setItem("cgims_schedules", JSON.stringify(schedules))
              this.retrieve.data = JSON.parse(localStorage.getItem("cgims_schedules"))

              setTimeout(() => {this.create.success = null}, 3000);
            })
            .catch((err) => {
              this.create.loading = false
              if (err.response.status == 401) userStore.signOut()
              else if (err.response.status == 406) this.create.error = err.response.data.error
              else this.create.error = "An error occured."
              console.log(err.response)
            })
        },
        async getSchedules() {
          const userStore = useUserStore()
          this.retrieve.loading = true
          this.retrieve.error = null

          await axios.get("staffs/me/schedules/", {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
            .then((resp) => {
              this.retrieve.loading = false
              this.retrieve.error = null
              localStorage.setItem("cgims_schedules", JSON.stringify(resp.data))
              this.retrieve.data = resp.data
            })
            .catch((err) => {
              this.retrieve.loading = false
              if (err.response.status == 401) userStore.signOut()
              else this.create.error = "An error occured."
              console.log(err.response)
            })
        },
        async deleteSchedule() {
          const userStore = useUserStore()
          this.delete.loading = true

          await axios.delete(`staffs/me/schedules/${this.delete.id}/delete/`, {headers: {"Authorization": `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
            .then((resp) => {
              // refresh the questionnaires list
              // this.getSchedules()
              const schedules = JSON.parse(localStorage.getItem("cgims_schedules"))
              schedules.splice(schedules.indexOf(schedules.find((she) => she.id == this.delete.id)), 1)
              localStorage.setItem("cgims_schedules", JSON.stringify(schedules))
              this.retrieve.data = JSON.parse(localStorage.getItem("cgims_schedules"))
              
              this.delete.loading = false
              this.delete.open = false
            })
            .catch((err) => {
                this.delete.loading = false
                if (err.response.status == 401) userStore.signOut()
                else if (err.response.status == 404) this.getSchedules()
                else this.create.error = "An error occured, please try again."
                console.log(err.response)
            })
        }
      }
})