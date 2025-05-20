import axios from 'axios';

// set base URL for all queries
axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.withCredentials = true; // cookies

// Settings CSRF-token
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

export default axios;