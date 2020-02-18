<template>
	
	<section id="events" class="pb-5">
		
		<div id="events_header" class="container">

			<div class="row mt-5">
                <div class="col-12">
                    <h1 class='m-about-title'><strong><span>Eventos</span></strong></h1>
                </div>
            </div>

		</div>

		<div id="events_content" class="container mt-5">


		</div>

	</section>

</template>

<script lang='ts'>

	import { Vue, Component } from 'vue-property-decorator';

	import EventsCarousel from '../components/EventsCarousel.vue';

	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class AboutView extends Vue {

		public images: string[] = ['header.jpg'];

		public returnClass(idx) : string {

			if (idx == 0)
				return "m-item carousel-item active";

			return "m-item carousel-item";
		}
	}

</script>

<style scoped>
	
	.m-about-title {
        text-align: center;
        color: #808080;
    }

    .m-about-text {
        text-align: center;
        color: #808080;
    }

</style>