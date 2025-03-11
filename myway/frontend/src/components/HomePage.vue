<template>
  <div class="home">
    <h1>Welcome to MyWay</h1>
    <ImageCarousel />
    <BestSellers />
    <StatisticsShow />
    <FeaturesList />
    <CarsPrologue />
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
</style>