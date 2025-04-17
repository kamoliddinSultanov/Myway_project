import axios from 'axios';

// Устанавливаем базовый URL для всех запросов
axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.withCredentials = true; // Включаем передачу cookies

// Настройка CSRF-токена (если используется)
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