<template>

	<div class="container my-4" v-if="hasEvents()">

		<!--Carousel Wrapper-->
		<div id="multi-item" class="carousel slide carousel-multi-item" data-ride="carousel">

			<!--Slides-->
			<div class="carousel-inner" role="listbox">

				<!--Slide-->
				<div v-bind:class="returnClass(index)" v-for="(p, index) in trio">

					<div class="row">

						<!--Card-->
						<div class="col-md-4" v-bind:class="returnCardClass(index)" v-for="event in p">
							<div class="card mb-2">
								<img v-bind:src="'/static/public/assets/cs/' + event.img" class='card-img-top'>

								<div class="card-body">
									<h4 class="card-title">{{event.name}}</h4>
									<p class="card-text">{{event.description[0] + " ..."}}</p>
									<a href="#" class='btn btn-primary m-btn'>Saber Mais</a>
								</div>

							</div>
						</div>
						<!--/.Card-->

					</div>

				</div>

			</div>
			<!--/.Slides-->

			<!--Controls-->
			<a class="carousel-control-prev m-controls" href="#multi-item" role="button" data-slide="prev">
				<a class="btn-floating" href="#multi-item" data-slide="prev" aria-hidden="true">
					<i class="fa fa-chevron-left"></i>
				</a>
				<span class="sr-only">Previous</span>
			</a>
			<a class="carousel-control-next m-controls" href="#multi-item" role="button" data-slide="next">
				<a class="btn-floating" href="#multi-item" data-slide="next" aria-hidden="true">
					<i class="fa fa-chevron-right"></i>
				</a>
				<span class="sr-only">Next</span>
			</a>
			<!--/.Controls-->

		</div>
		<!--/.Carousel Wrapper-->

	</div>

</template>

<script lang='ts'>
	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	interface Event {
		name: string;
		description: string;
		img: string;
	}

	@Component({})
	export default class EventsCarousel extends Vue {

		/*public events: Event[] = [
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'},
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'},
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'}
		];*/

		public lang: string = this.$store.getters.getLang;

		@Prop({ type: Array, required: true })
		public events: Event[];

		public trio: Event[][] = [];

		public generateCarousel() {

			this.trio = [];

			let n: number = 0;
			let c: number = 0;

			while(c < this.events.length) {
				this.trio.push([]);
				for (let i = 0; i < 3 && c < this.events.length; i++) {
					this.trio[n].push(this.events[c++]);
				}
				n++;
			}

		}

		@Watch('events')
		public onEventsUpdate(value, oldValue) {
			this.generateCarousel();
		}

		public returnClass(idx) : string {

			if (idx == 0)
				return "carousel-item active";

			return "carousel-item";
		}

		public returnCardClass(idx) : string {

			if (idx == 0)
				return "col-md-4";

			return "col-md-4 clearfix d-none d-md-block";
		}

		public hasEvents(): boolean {
			return this.events && this.events !== [] && this.events.length !== 0;
		}

	}
</script>

<style scoped>

	.m-btn {
		background-color: steelblue;
	}

	.m-controls {
		width: 2%;
	}

</style>
