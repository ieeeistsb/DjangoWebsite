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

			<p class='m-about-text'>
				<span>{{description}}</span>
			</p>

		</div>

		<div>

			<p class='m-about-text'>
				<span>O IEEE Computer Society é a maior sociedade internacional na área das Tecnologias da informação, dedicada a contribuir para o progresso desta área, através do aperfeiçoamento das capacidades da comunidade informática.
				</span>
			</p>

			<p class='m-about-text'>
				<span>Como membros deste student chapter no IEEE-IST, temos o objetivo de dar aos estudantes do IST ferramentas para o desenvolvimento de capacidades, que poderão ajudar no seu crescimento enquanto profissionais na área das Tecnologias da Informação, propondo-lhes iniciativas que o promovam.
				</span>
			</p>

			<p class='m-about-text'>
				<span>Com esta finalidade, temos vindo a oferecer workshops não só teóricos como práticos,de forma a aprofundar o conhecimento dos alunos de Informática; realizar competições dentro do IST, para criar e desenvolver o interesse dos estudantes e estabelecer uma plataforma que permita aos alunos pôr em prática as capacidades desenvolvidas.
				</span>
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

	import { Vue, Component } from 'vue-property-decorator';

	import EventsCarousel from '../components/EventsCarousel.vue';

	import app from '../api/store/modules/app.ts';

	import communities from '../api/store/modules/communities.ts';

	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class AboutView extends Vue {

		public images: string[] = ['header.jpg'];

		public description: string = '';

		public returnClass(idx) : string {

			if (idx == 0)
				return "m-item carousel-item active";

			return "m-item carousel-item";
		}

		public beforeMount() {
			/*let c = communities.getCommunities;
			console.debug(c);
			c.forEach((com) => {
				console.debug(com);
				if (com.tag == app.activeCommunity) {
					this.description = com.description;
				}
			});
			console.debug(this.description);*/
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