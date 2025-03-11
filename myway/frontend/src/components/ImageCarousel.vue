<template>
  <div class="carousel-container">
    <div class="carousel-wrapper" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
      <div class="carousel-slide" v-for="(img, index) in images" :key="index">
        <img :src="img.src" :alt="img.alt" class="carousel-image" />
      </div>
    </div>
    <button class="carousel-button prev" @click="prevSlide">‹</button>
    <button class="carousel-button next" @click="nextSlide">›</button>
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
    };
  },
  methods: {
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevSlide() {
      this.currentIndex =
        (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
  },
};
</script>

<style scoped>
.carousel-container {
  position: relative;
  overflow: hidden;
  width: 100%;
  max-width: 90%;
  margin: 0 auto;
}

.carousel-wrapper {
  display: flex;
  transition: transform 0.5s ease-in-out;
}

.carousel-slide {
  min-width: 100%;
  box-sizing: border-box;
}

.carousel-image {
  width: 100%;
  height: auto;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  z-index: 1;
}

.carousel-button.prev {
  left: 10px;
}

.carousel-button.next {
  right: 10px;
}
</style>