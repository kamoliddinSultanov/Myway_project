<template>
    <div class="login-form">
      <h2>Login</h2>
      <div v-if="error" class="error-message">
        {{ error }}
      </div>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>Username:</label>
          <input 
            type="text" 
            v-model="formData.username" 
            required
          >
        </div>
        <div class="form-group">
          <label>Password:</label>
          <input 
            type="password" 
            v-model="formData.password" 
            required
          >
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
      <div class="register-link">
        Don't have an account? 
        <router-link to="/register">Register here</router-link>
      </div>
    </div>
  </template>
  
  <script>
  import { reactive, ref } from 'vue'
  import { useStore } from 'vuex'
  import { useRouter } from 'vue-router'
  
  export default {
    name: 'LoginPage',
    setup() {
      const store = useStore()
      const router = useRouter()
      const error = ref('')
      const loading = ref(false)
  
      const formData = reactive({
        username: '',
        password: ''
      })
  
      const handleSubmit = async () => {
        try {
          loading.value = true
          error.value = ''
          
          const success = await store.dispatch('login', {
            username: formData.username,
            password: formData.password
          })
  
          if (success) {
            router.push('/')
          } else {
            error.value = 'Invalid credentials'
          }
        } catch (err) {
          error.value = err.response?.data?.error || 'Login failed'
          console.error('Login error:', err)
        } finally {
          loading.value = false
        }
      }
  
      return {
        formData,
        handleSubmit,
        error,
        loading
      }
    }
  }
  </script>
  
  <style scoped>
  .login-form {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 0.75rem;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  
  .error-message {
    color: #dc3545;
    margin-bottom: 1rem;
    padding: 0.5rem;
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
    border-radius: 4px;
  }
  
  .register-link {
    margin-top: 1rem;
    text-align: center;
  }
  
  .register-link a {
    color: #4CAF50;
    text-decoration: none;
  }
  
  .register-link a:hover {
    text-decoration: underline;
  }
  </style>