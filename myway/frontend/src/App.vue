<template>
  <div id="app">
    <MainNavbar />
    <router-view/>
    <FooterSection />
  </div>
</template>

<script>
import MainNavbar from './components/MainNavbar.vue'
import FooterSection from './components/FooterSection.vue';

export default {
  name: 'App',
  components: {
    MainNavbar,
    FooterSection,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>