import { createStore } from 'vuex';
import axios from 'axios'; // Убедитесь, что axios импортирован

const state = {
  user: null,
  isAuthenticated: false,
};

const mutations = {
  setUser(state, user) {
    state.user = user;
    state.isAuthenticated = !!user;
  },
};

const actions = {
  async getCSRFToken() {
    try {
      await axios.get('/api/csrf-token/');
    } catch (error) {
      console.error('Error fetching CSRF token:', error);
    }
  },
  async register({ commit }, userData) {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', userData)
        commit('SET_USER', response.data.user)
        return { success: true }
      } catch (error) {
        commit('SET_AUTH_ERROR', error.response.data)
        return { success: false, error: error.response.data }
      }
  },
  async login({ commit, dispatch }, credentials) {
    try {
      await dispatch('getCSRFToken');
      const response = await axios.post('/api/login/', credentials);
      commit('setUser', response.data);
      return true;
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },
  async logout({ commit, dispatch }) {
    try {
      await dispatch('getCSRFToken');
      await axios.post('/api/logout/');
      commit('setUser', null);
      return true;
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  },
  async checkAuth({ commit }) {
    try {
      const response = await axios.get('/api/user/');
      commit('setUser', response.data);
      return true;
    } catch (error) {
      commit('setUser', null);
      return false;
    }
  },
};

const getters = {
  isAuthenticated: (state) => state.isAuthenticated,
  user: (state) => state.user,
};

export default createStore({
  state,
  mutations,
  actions,
  getters,
});