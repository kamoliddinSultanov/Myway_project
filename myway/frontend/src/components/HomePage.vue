<template>
  <div class="home">
    <h1>Welcome to MyWay</h1>
    <ImageCarousel />
  </div>
</template>

<script>
import ImageCarousel from './ImageCarousel.vue';

export default {
  name: 'HomePage',
  components: {
    ImageCarousel,
  },
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}
</style>