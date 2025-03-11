<template>
  <div class="about-us">
    <h1>About Us</h1>
    <p>Learn more about MyWay.</p>
    <OurMission />
    <h2>Our Location</h2>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2998.7128549044846!2d69.2361988758811!3d41.2715876031704!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38ae8b9a4f3e2a85%3A0x1eb2c9fa957b784c!2sMy%20Way!5e0!3m2!1sru!2s!4v1741724277426!5m2!1sru!2s" width="1200" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</template>

<script>
import OurMission from './OurMission.vue';
export default {
  name: 'AboutUsPage',
  components: {
    OurMission,
  },
}
</script>

<style scoped>
.about-us {
  text-align: center;
  margin-top: 50px;
}
h2{
  font-size: 24px;
}
iframe{
  margin: 0 auto;
}
</style>