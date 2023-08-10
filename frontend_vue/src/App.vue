<template>
  <div id="app">
    <AppNavbar v-if="isAuthenticated" />

    <LandingNavbar v-else />


    <div class="flex justify-center items-center h-screen">
        <router-view />
    </div>

    <AppFooter />


  </div>
</template>

<style lang="scss">

html, body {
  height: 100%;
  background-color: white;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

  }
}
</style>



<script>
import AppNavbar from './components/AppNavbar.vue';
import LandingNavbar from './components/LandingNavbar.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  name: 'App',
  components: {
    AppNavbar,
    LandingNavbar,
    AppFooter,
  }
}
</script>
