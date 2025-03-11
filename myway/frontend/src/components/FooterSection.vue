<template>
    <footer class="flex flex-col space-y-10 justify-center m-10">

        <nav class="flex justify-center flex-wrap gap-6 text-gray-500 font-medium">
            <a class="hover:text-gray-900" href="#"><router-link to="/">Home</router-link></a>
            <a class="hover:text-gray-900" href="#"><router-link to="/catalogue">Car Catalogue</router-link></a>
            <a class="hover:text-gray-900" href="#"><router-link to="/about-us">About Us</router-link></a>
        </nav>

        <div class="flex justify-center space-x-5">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
                <img src="https://img.icons8.com/fluent/30/000000/facebook-new.png" />
            </a>
            <a href="https://t.me/autosaleuzb01" target="_blank" rel="noopener noreferrer">
                <img src="https://img.icons8.com/?size=30&id=63306&format=png&color=000000" />
            </a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
                <img src="https://img.icons8.com/fluent/30/000000/instagram-new.png" />
            </a>
        </div>
        <p class="text-center text-gray-700 font-medium">&copy; 2022 Company Ltd. All rights reservered.</p>
    </footer>
</template>
<script>
export default {
	name: 'FooterSection',
}
</script>