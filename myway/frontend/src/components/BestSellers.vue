<template>
  <section class="my-12 px-4">
    <h2 class="text-center text-3xl font-bold mb-8">Our Best Sellers</h2>
    <div class="flex flex-wrap justify-center items-center space-x-4 space-y-4 md:space-y-0 gap-20">
      <div v-for="(logo, index) in logos" :key="index" class="flex-shrink-0 w-24 h-24 md:w-32 md:h-32">
        <img :src="logo.src" :alt="logo.alt" class="w-full h-full object-contain" />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'BestSellers',
  data() {
    return {
      logos: [
        { src: require('@/assets/mercedes-logo.png'), alt: 'Logo 1' },
        { src: require('@/assets/bmw-logo.png'), alt: 'Logo 2' },
        { src: require('@/assets/audi-logo.png'), alt: 'Logo 3' },
        { src: require('@/assets/porsche-logo.png'), alt: 'Logo 4' },
        { src: require('@/assets/toyota-logo.png'), alt: 'Logo 5' },
      ],
    };
  },
};
</script>