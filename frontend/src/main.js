import { createApp, markRaw } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import axios from "axios";
import FlagIcon from "vue-flag-icon";
import VueTippy from "vue-tippy";
import { SetupCalendar } from "v-calendar";

import "./assets/index.css";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";
import "tippy.js/themes/translucent.css";
import "v-calendar/dist/style.css";

// axios settings
// axios.defaults.baseURL = "http://localhost:8000/api/";
// axios.defaults.baseURL = "http://192.168.1.102:8000/api/";
// docker
axios.defaults.baseURL = "http://192.168.0.2:80/api/";
axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;

// app instance
const app = createApp(App);

// insert router into stores
const pinia = createPinia();
pinia.use(({ store }) => {
  store.$router = markRaw(router);
});

// v-calender
app.use(SetupCalendar, {});

// tippy.js
app.use(
  VueTippy,
  // optional
  {
    directive: "tippy", // => v-tippy
    component: "tippy", // => <tippy/>
    componentSingleton: "tippy-singleton", // => <tippy-singleton/>,
    defaultProps: {
      placement: "top",
      allowHTML: true,
    }, // => Global default options * see all props
  }
);

// app.use(createPinia());
app.use(pinia);
app.use(router);
app.use(FlagIcon);

app.mount("#app");
