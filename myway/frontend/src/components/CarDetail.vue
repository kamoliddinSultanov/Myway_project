  <template>
    <div class="car-detail">
      <h1>{{ car.title }}</h1>
      <img :src="car.image" alt="Car Image" />
      <p><strong>Brand:</strong> {{ car.brand }}</p>
      <p><strong>Model:</strong> {{ car.model }}</p>
      <p><strong>Price:</strong> ${{ car.price }}</p>
      <p><strong>Description:</strong> {{ car.description }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'CarDetail',
    props: {
      id: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        car: {}
      };
    },
    created() {
      //const carId = this.$route.params.id;
      const carId = this.id;
      axios.get(`http://localhost:8000/api/cars/${carId}/`)
        .then(response => {
          this.car = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching the car details!', error);
        });
    },
  }
  </script>
  
  <style scoped>
  .car-detail {
    text-align: center;
    margin-top: 50px;
  }
  .car-detail img {
    width: 100%;
    height: auto;
  }
  </style>