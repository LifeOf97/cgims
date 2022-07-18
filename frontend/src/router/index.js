/* eslint-disable */
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

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
      path: "/signin",
      name: "signin",
      component: () => import("../views/SignIn.vue"),
      meta: {title: "CGIMS | Sign In"},
    },
    {
      path: "/staff",
      name: "staff",
      redirect: {name: 'staffdashboard'},
      component: () => import("../views/StaffAccount.vue"),
      children: [
        {
          path: "/staff",
          name: "staffdashboard",
          component: () => import("../components/AppStaffDashboard.vue"),
          meta: {title: "CGIMS | Staff Dashboard"},
        },
        {
          path: "/staff/questionnaires",
          name: "staffquestionnaires",
          component: () => import("../components/AppStaffQuestionnaire.vue"),
          meta: {title: "CGIMS | Staff Questionnaires"},
        },
        {
          path: "/staff/schedules",
          name: "staffschedules",
          component: () => import("../components/AppStaffSchedule.vue"),
          meta: {title: "CGIMS | Staff Schedules"},
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
  // const user = useUserStore()

  // if (to.meta.requiresAuth && !JSON.parse(localStorage.getItem('libex_token'))) {
  //   user.userSignIn.redirect = to.fullPath
  //   return {name: 'signin', query: {redirect: to.fullPath}}
  // }
})

export default router;
