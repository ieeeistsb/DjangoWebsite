<template>
	<div>
		<img src='../assets/landing/home.png' class='home-img'>

		<div id='about'>
			<p>&nbsp;</p>
			<h1 class='m-about-title'>
				<strong><span>IEEE-IST Student Branch</span></strong>
			</h1>
			<p>&nbsp;</p>
			<p class='m-about-text'>
				<span>O <strong>IEEE IST Student Branch</strong> é um grupo associativo autónomo do Instituto Superior Técnico e que faz parte da organização global IEEE. O seu foco é no desenvolvimento de iniciativas e eventos inovadores nas áreas que estão a faltar a educação académica, e que vão desde a formação em capacidades técnicas, até providenciar as melhores oportunidades de estágios.
				</span>
			</p>
			<p class='m-about-text'>
				<span>O IEEE IST Student Branch procura <strong>desenvolver e estimular um ambiente de desenvolvimento</strong> para todas as mentes criativas do Instituto Superior Técnico, independentemente da sua área de formação. Ao promover a criatividade nos seus membros, e focando a sua energia em fornecer as melhores oportunidades a toda a comunidade, o IEEE IST define o seu objetivo em formar da melhor forma possível a próxima geração.
				</span>
			</p>
			<p class='m-about-text'>
				<span>Formada por mais de <strong>60 membros</strong>, todos com uma paixão por partilhar o seu conhecimento e inspirar a próxima geração, a nossa equipa encontra-se dividida em 3 Chapters associados a Sociedades – Engineering in Medicine and Biology Society (EMBS), Industry and Automation Society (IAS) and Computer Society (CS), e em um Chapter associado a um Group Chapter – Womens in Engineering (WiE).
				</span>
			</p>
			<p>&nbsp;</p>

			<h1 class='m-about-title'>
				<strong><span>IEEE</span></strong>
			</h1>
			<p>&nbsp;</p>
			<p class='m-about-text'>
				<span>O IEEE (Institute of Electrical and Electronics Engineers), é a <strong>maior organização de profissionais técnicos</strong> dedicados ao avanço da Tecnologia para o benefício da Humanidade. Os seus membros inspiram a comunidade global a inovar com o objetivo de alcançar um futuro melhor, e concretizando-o através dos seus mais de <strong>423 000 membros</strong> oriundos de mais de <strong>160 países</strong>.
				</span>
			</p>
			<p class='m-about-text'>
				<span>Como definido na sua declaração de visão, o IEEE procura ser essencial para a comunidade técnica global e para a todos os profissionais técnicos em todo o mundo, e ainda tem por objetivo ser universalmente reconhecido pelas suas contribuições na tecnologia, assim como no melhoramento das condições globais para os técnicos profissionais. O IEEE é ainda suportado por mais de 40 sociedades, que vão desde a Sociedade para a Engenharia Aplicada à Medicina e à Biologia, até a Sociedade da Ciência de Computadores, que implementam a visão do IEEE através dos diversos campos que abrangem a Engenharia Eletrotécnica e Electrónica, e as suas aplicações.
				</span>
			</p>
		</div>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Eventos</span></strong>
		</h1>
		<p>&nbsp;</p>

		<events-carousel></events-carousel>

	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import EventsCarousel from '../components/EventsCarousel.vue';

 	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class HomeView extends Vue {

	}
</script>

<style scoped>

	.home-img {
		width: 100%;
		height: 100%;
	}

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

</style>