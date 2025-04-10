<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Заголовок и поиск -->
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-800 mb-2">Catalogue</h1>
      <p class="text-lg text-gray-600 mb-6">Welcome to the catalogue page of MyWay.</p>
      
      <div class="max-w-md mx-auto">
        <input
          v-model="searchQuery"
          @input="searchCars"
          placeholder="Search for cars..."
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
        />
      </div>
    </div>

    <!-- Список автомобилей -->
    <div class="mb-8">
      <h2 class="text-2xl font-semibold text-gray-800 mb-6">Available Cars</h2>
      
      <!-- Индикатор загрузки -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-green-500"></div>
        <p class="mt-4 text-gray-600">Loading cars...</p>
      </div>

      <!-- Результаты -->
      <div v-else>
        <!-- Сообщение если нет результатов -->
        <div v-if="cars.length === 0" class="text-center py-12 bg-gray-50 rounded-lg">
          <p class="text-xl text-gray-500">No cars found</p>
          <p v-if="searchQuery" class="text-gray-400 mt-2">Try another search term</p>
        </div>

        <!-- Список автомобилей -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="car in cars" :key="car.id" class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
            <!-- Изображение -->
            <div class="h-48 overflow-hidden">
              <img 
                :src="getFullImageUrl(car.image)" 
                :alt="car.title"
                class="w-full h-full object-cover"
              />
            </div>
            
            <!-- Информация -->
            <div class="p-6">
              <h3 class="text-xl font-bold text-gray-800 mb-1">{{ car.title }}</h3>
              <div class="flex items-center text-gray-600 mb-2">
                <span class="font-medium">{{ car.brand }}</span>
                <span class="mx-2">•</span>
                <span>{{ car.model }}</span>
              </div>
              
              <p class="text-gray-700 mb-4 line-clamp-2">{{ car.description }}</p>
              
              <div class="flex items-center justify-between">
                <span class="text-2xl font-bold text-green-600">${{ formatPrice(car.price) }}</span>
                <router-link 
                  v-if="car.id" 
                  :to="{ name: 'CarDetail', params: { id: car.id } }"
                  class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition"
                >
                  View Details
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CataloguePage',
  data() {
    return {
      cars: [],
      searchQuery: '',
      loading: false,
      baseApiUrl: 'http://localhost:8000/api'
    };
  },
  created() {
    this.fetchCars();
  },
  methods: {
    fetchCars() {
      this.loading = true;
      axios.get(`${this.baseApiUrl}/cars/`)
        .then(response => {
          this.cars = response.data;
        })
        .catch(error => {
          console.error('Error fetching cars:', error);
          this.cars = [];
        })
        .finally(() => {
          this.loading = false;
        });
    },
    searchCars() {
      if (this.searchQuery.trim() === '') {
        this.fetchCars();
        return;
      }
      
      this.loading = true;
      axios.get(`${this.baseApiUrl}/search/`, {
        params: { q: this.searchQuery }
      })
        .then(response => {
          this.cars = response.data;
        })
        .catch(error => {
          console.error('Search error:', error);
          this.cars = [];
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getFullImageUrl(imagePath) {
      if (!imagePath) return '';
      return imagePath.startsWith('http') ? imagePath : `http://localhost:8000${imagePath}`;
    },
    formatPrice(price) {
      return parseFloat(price).toLocaleString();
    }
  }
}
</script>

<style>
/* Анимация для индикатора загрузки */
@keyframes spin {
  to { transform: rotate(360deg); }
}
.animate-spin {
  animation: spin 1s linear infinite;
}

/* Обрезание длинного текста */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Плавные переходы */
.transition {
  transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
</style>