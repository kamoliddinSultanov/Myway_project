<template>
  <nav class="navbar">
    <ul class="nav-left">
      <li>
        <router-link to="/">
          <img src="@/assets/logocar.svg" alt="Logo" class="logo" />
        </router-link>
      </li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/catalogue">Catalogue</router-link></li>
      <li><router-link to="/about-us">About Us</router-link></li>
    </ul>
    <ul class="nav-right">
      <template v-if="!isAuth">
        <li><router-link to="/login" class="auth-link">Login</router-link></li>
        <li><router-link to="/register" class="auth-link">Register</router-link></li>
      </template>
      <template v-else>
        <li class="user-info">
          <span class="username">{{ currentUser }}</span>
        </li>
        <li><button @click="handleLogout" class="logout-btn">Logout</button></li>
      </template>
    </ul>
  </nav>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'MainNavbar',
  setup() {
    const store = useStore()
    const router = useRouter()

    // Используем computed для реактивных свойств
    const isAuth = computed(() => store.state.isAuthenticated)
    const currentUser = computed(() => store.state.user?.username)

    const handleLogout = async () => {
      try {
        await store.dispatch('logout')
        router.push('/login')
      } catch (err) {
        console.error('Logout failed:', err)
      }
    }

    return {
      isAuth,
      currentUser,
      handleLogout
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: #333;
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
}

.nav-left, .nav-right {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
}

.navbar li {
  float: left;
}

.navbar li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar li a:hover {
  background-color: #111;
}

.logo {
  width: 110px;
  height: 15px;
}

.auth-link {
  color: #fff;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.auth-link:hover {
  background-color: #444;
}

.logout-btn {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  margin: 8px;
  transition: background-color 0.3s;
}

.logout-btn:hover {
  background-color: #c82333;
}

.user-info {
  color: #fff;
  padding: 14px 16px;
  display: flex;
  align-items: center;
}

.username {
  color: #fff;
  margin-right: 10px;
}
</style>