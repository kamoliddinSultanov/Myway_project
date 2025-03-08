<template>
  <nav class="navbar">
    <ul>
      <li>
        <router-link to="/">
          <img src="@/assets/logocar.svg" alt="Logo" class="logo" />
        </router-link>
      </li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/catalogue">Catalogue</router-link></li>
      <li><router-link to="/about-us">About Us</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'MainNavbar'
}
</script>

<style scoped>
.navbar {
  background-color: #333;
  overflow: hidden;
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
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
</style>