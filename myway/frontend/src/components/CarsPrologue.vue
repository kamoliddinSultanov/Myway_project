
<template>
	<section>
        <!-- Container -->
        <div class="mx-auto w-full max-w-7xl px-5 py-16 md:px-10 md:py-20">
            <!-- Component -->
            <div class="flex flex-col items-start gap-8 sm:gap-20 md:flex-row md:items-center">
                <div class="md:w-1/2">
                    <h2 class="mb-4 max-w-3xl text-3xl font-bold md:text-5xl">
                        Checkout the car catalogue
                    </h2>
                    <p class="mb-6 max-w-lg text-sm text-gray-500 sm:text-base md:mb-10">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit ut
                        aliquam, purus sit amet luctus venenatis, lectus
                    </p>
                    <a href="javascript:void(0);" class="inline-block bg-black px-6 py-3 font-semibold text-white">
                        <router-link to="/catalogue">Get Started</router-link>
                    </a>
                </div>
                <div class="md:w-1/2">
                    <img src="https://firebasestorage.googleapis.com/v0/b/flowspark-1f3e0.appspot.com/o/Tailspark%20Images%2FPlaceholder%20Image.svg?alt=media&token=375a1ea3-a8b6-4d63-b975-aac8d0174074" alt="" />
                </div>
            </div>
        </div>
	</section>
</template>
<script>
export default {
	name: 'CarsPrologue',
}
</script>
