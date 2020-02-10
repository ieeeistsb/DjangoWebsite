<template>
	<div>
		<div id='imgsCarousel' class='carousel slide' data-ride='carousel'>
			
			<div class='carousel-inner'>
				<div v-bind:class="returnClass(index)" v-for='(img, index) in images'>

					<img v-bind:src="'/static/public/assets/cs/' + img" class='card-img-top d-block w-100'>

				</div>

			</div>

			<a class="carousel-control-prev" href="#imgsCarousel" role="button" data-slide="prev">
				<span class="carousel-control-prev-icon" aria-hidden="true"></span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="carousel-control-next" href="#imgsCarousel" role="button" data-slide="next">
				<span class="carousel-control-next-icon" aria-hidden="true"></span>
				<span class="sr-only">Next</span>
			</a>

		</div>

		<p>&nbsp;</p>

		<div>

			<p class='m-about-text' v-for='paragraph in getDescription()'>
				<span>{{paragraph}}</span>
			</p>

		</div>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Eventos</span></strong>
		</h1>
		<p>&nbsp;</p>

		<events-carousel/>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import EventsCarousel from '../components/EventsCarousel.vue';

	import CommunityModule from '../api/store/modules/community.ts';

	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class AboutView extends Vue {

		@Prop({required: true})
		public tag: string;

		public images: string[] = ['header.jpg'];

		public returnClass(idx) : string {

			if (idx == 0)
				return "m-item carousel-item active";

			return "m-item carousel-item";
		}

		public getDescription() {

			const community_module = new CommunityModule(this.tag);

			return community_module.description;
		}

	}

</script>

<style scoped>
	
	.m-about-title {
		text-align: center;
		color: #808080;
	}

	.m-about-text {
		text-align: justify;
		color: #808080;
		margin-left: 10%;
		margin-right: 10%;
	}

	#imgsCarousel {
		margin-left: 10%;
		margin-right: 10%;
	}

	.carousel-inner > .m-item > img {
		width:640px;
		height:360px;
	}

</style>