<template>
	
	<section id="events" class="pb-5">
		
		<div class="container">

			<div id='imgsCarousel' class='carousel slide' data-ride='carousel'>
			
				<div class='carousel-inner'>
					<div v-bind:class="returnClass(index)" v-for='(img, index) in getImages()'>

						<img v-bind:src="img" class='card-img-top d-block w-100'>

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
		
		</div>

		<div id="events_header" class="container" v-if="hasEvents()">

			<div class="row mt-5">
           	    <div class="col-12">
           	        <h1 class='m-about-title'>
           	        	<strong>
           	        		<span v-if="lang==='pt'">Eventos</span>
           	        		<span v-else>Events</span>
           	        	</strong>
           	        </h1>
           	    </div>
           	</div>

		</div>

		<events-carousel :events="events"/>

	</section>

</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import EventsCarousel from '../components/EventsCarousel.vue';

	import { Community } from '../api/entities.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	import CommunityModule from '../api/storage/modules/community.ts';

	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class AboutView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public lang: string = this.$store.getters.getLang;

		public events: Event[] = [];

		async created() {
			try {
				this.events = (await CommunityApi.get_community_events(this.tag, this.lang)).reverse();
			} catch(error) {
				alert(error);
			}
		}

		@Watch('tag')
		public async onTagUpdate(value, oldValue) {
			try {
				this.events = (await CommunityApi.get_community_events(this.tag, this.lang)).reverse();
			} catch(error) {
				alert(error);
			}
		}

		public returnClass(idx) : string {

			if (idx == 0)
				return "m-item carousel-item active";

			return "m-item carousel-item";
		}

		public getDescription() {

			const community_module = new CommunityModule(this.tag);

			return community_module.description;
		}

		public getImages() {

			const community_module = new CommunityModule(this.tag);

			return community_module.images;
		}

		public hasEvents(): boolean {
			return this.events && this.events !== [] && this.events.length !== 0;
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
    }

</style>