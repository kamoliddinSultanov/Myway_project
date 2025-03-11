<template>
  <div class="relative overflow-hidden">
    <div class="flex transition-transform duration-500 ease-in-out" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div class="min-w-full h-70" v-for="(img, index) in images" :key="index">
        <img :src="img.src" :alt="img.alt" class="w-full h-full object-cover" />
      </div>
    </div>
    <button class="absolute top-1/2 left-4 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded" @click="prevSlide">‹</button>
    <button class="absolute top-1/2 right-4 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded" @click="nextSlide">›</button>
    <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
      <button
        v-for="(img, index) in images"
        :key="index"
        class="w-4 h-4 rounded-full"
        :class="{ 'bg-gray-800': currentIndex === index, 'bg-gray-400': currentIndex !== index }"
        @click="goToSlide(index)">
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageCarousel',
  data() {
    return {
      currentIndex: 0,
      images: [
        { src: require('@/assets/image1.jpg'), alt: 'Image 1' },
        { src: require('@/assets/image2.jpg'), alt: 'Image 2' },
        { src: require('@/assets/image3.jpg'), alt: 'Image 3' },
      ],
      interval: null,
    };
  },
  mounted() {
    this.startAutoSlide();
  },
  beforeUnmount() {
    this.stopAutoSlide();
  },
  methods: {
    startAutoSlide() {
      this.interval = setInterval(this.nextSlide, 3000);
    },
    stopAutoSlide() {
      clearInterval(this.interval);
    },
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevSlide() {
      this.currentIndex =
        (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
    goToSlide(index) {
      this.currentIndex = index;
    },
  },
};
</script>