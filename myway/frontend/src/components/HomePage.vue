<template>
  <div class="home">
    <h1>Welcome to MyWay</h1>
    <ImageCarousel />
    <BestSellers />
    <StatisticsShow />
    <FeaturesList />
    <CarsPrologue />



    <div class="sketchfab-embed-wrapper"> <iframe title="Daewoo Matiz turbo" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/b7aafdf572914452a6e4c1858c3f4e9c/embed" width="1000" height="440"> </iframe> </div>

  </div>
</template>

<script>
import ImageCarousel from './ImageCarousel.vue';
import BestSellers from './BestSellers.vue';
import StatisticsShow from './StatisticsShow.vue';
import FeaturesList from './FeaturesList.vue';
import CarsPrologue from './CarsPrologue.vue';

export default {
  name: 'HomePage',
  components: {
    ImageCarousel,
    BestSellers,
    StatisticsShow,
    FeaturesList,
    CarsPrologue,
  },
};
</script>

<style scoped>
.home {
  text-align: center;
}


.sketchfab-embed-wrapper{
  display: flex;
  justify-content: center;
  
  
  
}
</style>