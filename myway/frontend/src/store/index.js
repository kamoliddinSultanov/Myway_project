import { createStore } from 'vuex'
import axios from 'axios'

// Базовая конфигурация axios
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.withCredentials = true

// Перехватчик для установки CSRF токена
axios.interceptors.request.use(
  config => {
    const csrfToken = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1]
    
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

export default createStore({
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    setUser(state, user) {
      state.user = user
      state.isAuthenticated = !!user
    }
  },
  actions: {
    async getCSRFToken() {
      try {
        await axios.get('/api/csrf-token/')
      } catch (error) {
        console.error('Error fetching CSRF token:', error)
      }
    },
    async register(_, userData) {
      try {
        await this.dispatch('getCSRFToken')
        await axios.post('/api/register/', userData)
        return true
      } catch (error) {
        console.error('Registration error:', error)
        throw error
      }
    },
    async login({ commit }, credentials) {
      try {
        await this.dispatch('getCSRFToken')
        const response = await axios.post('/api/login/', credentials)
        commit('setUser', response.data)
        return true
      } catch (error) {
        console.error('Login error:', error)
        throw error
      }
    },
    async logout({ commit }) {
      try {
        await this.dispatch('getCSRFToken')
        await axios.post('/api/logout/')
        commit('setUser', null)
        return true
      } catch (error) {
        console.error('Logout error:', error)
        throw error
      }
    },
    async checkAuth({ commit }) {
      try {
        const response = await axios.get('/api/user/')
        commit('setUser', response.data)
        return true
      } catch (error) {
        commit('setUser', null)
        return false
      }
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    user: state => state.user
  }
})