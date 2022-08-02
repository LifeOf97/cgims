/* eslint-disable */
import { defineStore } from "pinia";
import { useStaffQuestionnaireStore } from "./staffQuestionnaire";
import { useStaffScheduleStore } from "./staffSchedule";
import { useStudentStore } from "./staffStudents";
import axios from "axios";


export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    userData: {
      loading: false,
      data: JSON.parse(localStorage.getItem("cgims_user")),
      error: null
    },
    userSignIn: {
      loading: false,
      access: JSON.parse(localStorage.getItem("cgims_access")),
      refresh: JSON.parse(localStorage.getItem("cgims_refresh")),
      username: JSON.parse(localStorage.getItem("cgims_username")),
      staffId: JSON.parse(localStorage.getItem("cgims_staffid")),
      success: false,
      redirect: null,
      error: null
    },
    userSignOut: {open: false}
  }),
  actions: {
    async signIn(data) {
      const questionnaireStore = useStaffQuestionnaireStore()
      const scheduleStore = useStaffScheduleStore()
      const studentStore = useStudentStore()
      this.userSignIn.loading = true
      this.userSignIn.success = false
      this.userSignIn.error = null

      await axios.post('auth/token/signin/', data)
        .then((resp) => {
          this.userSignIn.success = true
          this.userSignIn.error = null
          localStorage.setItem("cgims_access", JSON.stringify(resp.data['access']))
          localStorage.setItem("cgims_refresh", JSON.stringify(resp.data['refresh']))
          localStorage.setItem("cgims_staffid", JSON.stringify(data['username']))
          this.userSignIn.access = JSON.parse(localStorage.getItem("cgims_access"))
          this.userSignIn.refresh = JSON.parse(localStorage.getItem("cgims_refresh"))
          
          // check if user marked rememberMe
          if (data.rememberMe) {
            localStorage.setItem("cgims_username", JSON.stringify(data['username']))
            this.userSignIn.refresh = JSON.parse(localStorage.getItem("cgims_refresh"))
          }
          else localStorage.removeItem("cgims_username")

          // get the staff data
          this.getMe()
          questionnaireStore.getQuestionnaires()
          questionnaireStore.getPredefinedQuestionnaires()
          scheduleStore.getSchedules()
          studentStore.getStudents()

          // then redirect to initially requested page or dashboard
          setTimeout(() => {
            if (this.userSignIn.redirect) this.$router.push({name: this.userSignIn.redirect, params: {staffId: JSON.parse(localStorage.getItem("cgims_staffid"))}})
            else this.$router.push({name: 'staff', params: {staffId: JSON.parse(localStorage.getItem("cgims_staffid"))}})
            this.userSignIn.loading = false
            this.userSignIn.success = false
          }, 1000);

        })
        .catch((err) => {
          this.userSignIn.loading = false
          this.userSignIn.success = false

          if (err.response.status == 401) this.userSignIn.error = "Incorrect Staff_id/password"
          else this.userSignIn.error = "An error occured, please try again."
          console.log(err.response)
        })
    },
    async getMe() {
      this.userData.loading = true
      this.userData.error = null

      await axios.get('staffs/me/', {headers: { 'Authorization': `Bearer ${JSON.parse(localStorage.getItem('cgims_access'))}` } })
        .then((resp) => {
          this.userData.loading = false
          localStorage.setItem("cgims_user", JSON.stringify(resp.data))
          this.userData.data = JSON.parse(localStorage.getItem("cgims_user"))
        })
        .catch((err) => {
          this.userData.loading = false
          if (err.response.status == 401) this.signOut()
          else this.create.error = "An error occured."
          console.log(err.response)
        })
    },
    async signOut() {
      localStorage.removeItem('cgims_access')
      localStorage.removeItem('cgims_refresh')
      localStorage.removeItem('cgims_user')
      localStorage.removeItem('cgims_questionnaires')
      localStorage.removeItem('cgims_schedules')
      localStorage.removeItem('cgims_students')
      this.userSignOut.open = false
      this.$router.push({name: 'signinstaff'})
  },
  },
});
