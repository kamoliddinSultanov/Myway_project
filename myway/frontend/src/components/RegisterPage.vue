<template>
    <div class="register-form">
      <h2>Register</h2>
      <div v-if="error" class="error-message">{{ error }}</div>
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
          <label>Email:</label>
          <input 
            type="email" 
            v-model="formData.email" 
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
        <div class="form-group">
          <label>Confirm Password:</label>
          <input 
            type="password" 
            v-model="formData.password2" 
            required
          >
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Registering...' : 'Register' }}
        </button>
      </form>
      <div class="login-link">
        Already have an account? 
        <router-link to="/login">Login here</router-link>
      </div>
    </div>
  </template>
  
  <script>
  import { reactive, ref } from 'vue'
  import { useStore } from 'vuex'
  import { useRouter } from 'vue-router'
  
  export default {
    name: 'RegisterPage',
    setup() {
      const store = useStore()
      const router = useRouter()
      const error = ref('')
      const loading = ref(false)
  
      const formData = reactive({
        username: '',
        email: '',
        password: '',
        password2: ''
      })
  
      const handleSubmit = async () => {
        try {
          if (formData.password !== formData.password2) {
            error.value = "Passwords don't match"
            return
          }
  
          loading.value = true
          error.value = ''
  
          const success = await store.dispatch('register', formData)
          if (success) {
            router.push('/login')
          }
        } catch (err) {
          error.value = err.response?.data?.error || 'Registration failed'
          console.error('Registration error:', err)
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
  .register-form {
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
  
  .login-link {
    margin-top: 1rem;
    text-align: center;
  }
  
  .login-link a {
    color: #4CAF50;
    text-decoration: none;
  }
  
  .login-link a:hover {
    text-decoration: underline;
  }
  </style>