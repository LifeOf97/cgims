/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "../stores/user";
import HomeView from "../views/HomeView.vue";
import StaffAccount from "../views/StaffAccount.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {title: "CGIMS | Home"},
    },
    {
      path: "/signin/staff",
      name: "signinstaff",
      component: () => import("../views/SignIn.vue"),
      meta: {title: "CGIMS | Sign In"},
    },
    {
      path: "/:staffId",
      name: "staff",
      redirect: {name: 'staffdashboard'},
      component: StaffAccount,
      props: true,
      meta: {requiresAuth: true},
      children: [
        {
          path: "dashboard",
          name: "staffdashboard",
          component: () => import("../components/AppStaffDashboard.vue"),
          meta: {requiresAuth: true, title: "CGIMS | Staff Dashboard"},
        },
        {
          path: "myquestionnaires",
          name: "staffquestionnaires",
          component: () => import("../components/AppStaffQuestionnaire.vue"),
          meta: {requiresAuth: true, title: "CGIMS | Staff Questionnaires"},
        },
        {
          path: "myschedules",
          name: "staffschedules",
          component: () => import("../components/AppStaffSchedule.vue"),
          meta: {requiresAuth: true, title: "CGIMS | Staff Schedules"},
        },
        {
          path: "mystudents",
          name: "staffstudents",
          redirect: {name: 'staffstudentlist'},
          component: () => import("../components/AppStaffStudent.vue"),
          children: [
            {
              path: "",
              name: "staffstudentlist",
              component: () => import("../components/AppStaffStudentList.vue"),
              meta: {requiresAuth: true, title: "CGIMS | Staff Assigned Students"},
            },
            {
              path: ":department/:class/:regNo",
              name: "staffstudentsdata",
              component: () => import("../components/AppStaffStudentData.vue"),
              props: true,
              meta: {requiresAuth: true, title: "CGIMS | Student data"},
            },
          ]
        },
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'notfound',
      component: () => import("../components/NotFound.vue"),
      meta: {title: "CGIMS | 404 | Not Found"},
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) return {el: to.hash,  behavior: "smooth"}
    else {
      document.getElementById("staffView").scrollIntoView({behavior: 'smooth'})
      // document.getElementById("studentView").scrollIntoView({behavior: 'smooth'})
    }
    // else return { top: 0, behavior: "smooth" }
  }
});

router.beforeEach((to, from) => {
  // update the page title
  document.title = to.meta.title;
  const user = useUserStore()

  // make sure request is authenticated or redirect
  if (to.meta.requiresAuth && !JSON.parse(localStorage.getItem('cgims_access'))) {
    user.userSignIn.redirect = to.name
    return {name: 'signinstaff', query: {redirect: to.fullPath}}
  }
})

export default router;
