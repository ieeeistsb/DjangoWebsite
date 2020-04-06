<template>

	<div id='eventsCarousel' class='carousel slide' data-ride='carousel'>
			
		<div class='carousel-inner'>

			<div v-bind:class="returnClass(index)" v-for='(p, index) in poker'>
					
				<div class='card m-events-card' v-for='event in p'>
					<img v-bind:src="'/static/public/assets/cs/' + event.img" class='card-img-top m-card-img'>
					<div class='card-body'>
						<h5 class='card-title'>{{event.name}}</h5>
						<p class='card-text'>{{event.description}}</p>
						<a href='#' class='btn btn-primary m-btn'>Saber Mais</a>
					</div>
				</div>

			</div>

		</div>

		<a class="carousel-control-prev" href="#eventsCarousel" role="button" data-slide="prev">
				<span class="carousel-control-prev-icon" aria-hidden="true"></span>
				<span class="sr-only">Previous</span>
		</a>
		<a class="carousel-control-next" href="#eventsCarousel" role="button" data-slide="next">
			<span class="carousel-control-next-icon" aria-hidden="true"></span>
			<span class="sr-only">Next</span>
		</a>

	</div>

</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import BranchApi from '../api/BranchApi.ts';

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

		public events: Event[] = [];

		public poker: Event[][] = [];

		public generateCarousel() {

			let n: number = 0;
			let c: number = 0;

			while(c < this.events.length) {
				this.poker.push([]);
				for (let i = 0; i < 4 && c < this.events.length; i++) {
					this.poker[n].push(this.events[c++]);
				}
				n++;
			}

		}

		async created() {

			this.events = (await BranchApi.get_branch_events(this.lang)).reverse();

			this.generateCarousel();
		}

		public returnClass(idx) : string {

			if (idx == 0)
				return "carousel-item active";

			return "carousel-item";
		}

	}
</script>

<style scoped>

	#eventsCarousel {
		height: 450px;
		margin-left: 10%;
		margin-right: 10%;
	}

	.m-events-img {
		width: 100%;
		height: 50px;
	}

	.m-events-card {
		width: 18rem;
		margin: 3%;
		display: inline-block;
	}

	.m-card-img {
		width: 286px;
		height: 160px;
	}

	.m-btn {
		background-color: steelblue;
	}

</style>
