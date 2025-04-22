import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';


store.dispatch('checkAuth');


axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.withCredentials = true;

axios.interceptors.request.use(
  (config) => {
    const csrfToken = document.cookie
      .split('; ')
      .find((row) => row.startsWith('csrftoken='))
      ?.split('=')[1];

    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

//createApp(App).use(router).use(store).mount('#app')
const app = createApp(App);
app.use(store); 
app.use(router); 
app.mount('#app');
