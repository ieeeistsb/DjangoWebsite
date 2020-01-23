<template>
	<div>
		<div id='imgsCarousel' class='carousel slide' data-ride='carousel'>
			
			<div class='carousel-inner'>
				<div v-bind:class="'m-item carousel-item' + img == images[0] ? 'active' : ''" v-for='img in images'>

					<img v-bind:src="'/static/public/assets/cs/' + img" class='card-img-top'>

				</div>

			</div>

		</div>

		<p>&nbsp;</p>

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

	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class AboutView extends Vue {

		public images: string[] = ['header.jpg'];

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