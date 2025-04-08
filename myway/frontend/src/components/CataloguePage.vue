<template>
  <div class="catalogue">
    <h1>Catalogue</h1>
    <p>Welcome to the catalogue page of MyWay.</p>
  </div>
  <div>
    <h1>Cars</h1>
    <ul>
      <li v-for="car in cars" :key="car.id" style="display: flex;justify-content: center;align-items: center;">
        <img :src="car.image" alt="Car Image" width="100px" height="50px"/>
        {{ car.title }} - {{ car.brand }} - {{ car.model }} - ${{ car.price }} -
        <router-link :to="{ name: 'CarDetail', params: { id: car.id } }">View more</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'CataloguePage',
  data() {
    return {
      cars: []
    };
  },
  created() {
    axios.get('http://localhost:8000/api/cars/')
      .then(response => {
        this.cars = response.data;
      })
      .catch(error => {
        console.error('There was an error fetching the cars!', error);
      });
  },
}
</script>

<style scoped>
.catalogue {
  text-align: center;
  margin-top: 50px;
}
</style>