<template>
  <div class="max-w-7xl mx-auto px-4 py-8" v-if="car">
    <!-- Основная секция с машиной -->
    <div class="flex flex-col lg:flex-row gap-8 mb-12">
      <!-- Картинка слева -->
      <div class="lg:w-1/2">
        <img
          :src="getImageUrl(car.image)"
          :alt="car.title"
          class="w-full h-auto rounded-xl shadow-lg object-cover"
        />
      </div>

      <!-- Детали справа -->
      <div class="lg:w-1/2">
        <div class="bg-white p-8 rounded-xl shadow-lg">
          <h1 class="text-4xl font-bold text-gray-900 mb-4">{{ car.title }}</h1>

          <div class="grid grid-cols-2 gap-4 mb-6">
            <div>
              <p class="text-sm text-gray-500">Brand</p>
              <p class="text-lg font-medium">{{ car.brand }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-500">Model</p>
              <p class="text-lg font-medium">{{ car.model }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-500">Price</p>
              <p class="text-2xl font-bold text-blue-600">${{ formatPrice(car.price) }}</p>
            </div>
          </div>

          <button
            @click="handleRequestOrder"
            class="w-full py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-300"
          >
            Request Order
          </button>
        </div>
      </div>
    </div>

    <!-- Описание -->
    <div class="bg-white p-8 rounded-xl shadow-lg mb-8">
      <h2 class="text-2xl font-semibold text-gray-900 mb-4">Description</h2>
      <p class="text-gray-700 leading-relaxed">{{ car.description }}</p>
    </div>

    <!-- Модальное окно для заказа (только для авторизованных) -->
    <div v-if="isAuthenticated && showForm" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-xl shadow-xl w-full max-w-md">
        <!-- Заголовок и кнопка закрытия -->
        <div class="flex justify-between items-center border-b p-4">
          <h3 class="text-xl font-semibold">Order Request</h3>
          <button @click="showForm = false" class="text-gray-500 hover:text-gray-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Форма -->
        <form @submit.prevent="submitOrder" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
            <input
              v-model="orderForm.name"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input
              v-model="orderForm.email"
              type="email"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Phone</label>
            <input
              v-model="orderForm.phone"
              type="tel"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500"
            >
          </div>

          <button
            type="submit"
            class="w-full py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-300"
          >
            Submit Order
          </button>
        </form>
      </div>
    </div>

    <!-- Уведомление о необходимости авторизации -->
    <div v-if="authModalVisible" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-xl shadow-xl w-full max-w-md p-6">
        <h3 class="text-xl font-semibold mb-4">Authorization Required</h3>
        <p class="text-gray-700 mb-6">You need to login to place an order.</p>
        <div class="flex justify-end space-x-3">
          <button
            @click="authModalVisible = false"
            class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50"
          >
            Cancel
          </button>
          <button
            @click="redirectToLogin"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Лоадер -->
  <div v-else class="flex justify-center items-center h-64">
    <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      car: null,
      isAuthenticated: false,
      showForm: false,
      authModalVisible: false, // Для показа модалки авторизации
      orderForm: {
        name: '',
        email: '',
        phone: '',
      },
    };
  },
  async created() {
    await this.fetchCar();
    await this.checkAuth();
  },
  methods: {
    async fetchCar() {
      try {
        const carId = this.$route.params.id;
        const response = await axios.get(`http://localhost:8000/api/cars/${carId}/`);
        this.car = response.data;
      } catch (error) {
        console.error('Error fetching car:', error);
        this.$router.push('/catalogue');
      }
    },
    getImageUrl(imagePath) {
      if (!imagePath) return '';
      return imagePath.startsWith('http') ? imagePath : `http://localhost:8000${imagePath}`;
    },
    formatPrice(price) {
      return parseFloat(price).toLocaleString();
    },
    async checkAuth() {
      try {
        const response = await axios.get('http://localhost:8000/api/authenticated/', {
          withCredentials: true
        });
        this.isAuthenticated = response.data.isAuthenticated;
      } catch (error) {
        console.error('Auth check error:', error);
        this.isAuthenticated = false;
      }
    },
    async handleRequestOrder() {
      // Всегда проверяем актуальный статус перед действием
      await this.checkAuth();

      if (this.isAuthenticated) {
        // Показываем форму заказа
        this.showForm = true;
        this.authModalVisible = false;
      } else {
        // Показываем модалку с предложением авторизоваться
        this.authModalVisible = true;
        this.showForm = false;
      }
    },
    redirectToLogin() {
      this.authModalVisible = false;
      this.$router.push({ name: 'LoginPage' });
    },
    async submitOrder() {
      try {
        const payload = {
          ...this.orderForm,
          car: {
            title: this.car.title,
            brand: this.car.brand,
            model: this.car.model,
            price: this.car.price,
            description: this.car.description
          }
        };

        await axios.post(
          'http://localhost:8000/api/request-order/',
          payload,
          { withCredentials: true }
        );

        alert('Order submitted successfully!');
        this.showForm = false;
        this.orderForm = { name: '', email: '', phone: '' };

      } catch (error) {
        if (error.response?.status === 401) {
          this.isAuthenticated = false;
          this.showForm = false;
          this.$router.push('/login');
        } else {
          alert('Error: ' + (error.response?.data?.message || 'Order submission failed'));
        }
      }
    }

  },
};
</script>

<style scoped>
/* Плавная анимация для модальных окон */
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.3s ease;
}
.modal-enter-from, .modal-leave-to {
  opacity: 0;
}

/* Кастомные стили для скролла */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f1f1;
}
::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>