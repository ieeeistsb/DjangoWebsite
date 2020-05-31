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
				<span v-if="lang==='pt'">O <strong>IEEE IST Student Branch</strong> é um grupo associativo autónomo do Instituto Superior Técnico e que faz parte da organização global IEEE. O seu foco é no desenvolvimento de iniciativas e eventos inovadores nas áreas que estão a faltar a educação académica, e que vão desde a formação em capacidades técnicas, até providenciar as melhores oportunidades de estágios.
				</span>
				<span v-else>The <strong>IEEE IST Student Branch</strong> is an autonomous membership group of the Instituto Superior Técnico and part of the global IEEE organization. Its focus is on developing innovative initiatives and events in areas that are lacking academic education, ranging from training in technical skills, to providing the best internship opportunities.
				</span>
			</p>
			<p class='m-about-text'>
				<span v-if="lang==='pt'">O IEEE IST Student Branch procura <strong>desenvolver e estimular um ambiente de desenvolvimento</strong> para todas as mentes criativas do Instituto Superior Técnico, independentemente da sua área de formação. Ao promover a criatividade nos seus membros, e focando a sua energia em fornecer as melhores oportunidades a toda a comunidade, o IEEE IST define o seu objetivo em formar da melhor forma possível a próxima geração.
				</span>
				<span v-else>The IEEE IST Student Branch seeks to <strong>develop and stimulate a development environment</strong> for all creative minds at Instituto Superior Técnico, regardless of their area of ​​training. By promoting creativity in its members, and focusing its energy on providing the best opportunities for the entire community, the IEEE IST defines its goal to better shape the next generation.
				</span>
			</p>
			<p class='m-about-text'>
				<span v-if="lang==='pt'">Formada por mais de <strong>60 membros</strong>, todos com uma paixão por partilhar o seu conhecimento e inspirar a próxima geração, a nossa equipa encontra-se dividida em 3 Chapters associados a Sociedades – Engineering in Medicine and Biology Society (EMBS), Industry and Automation Society (IAS) and Computer Society (CS), e em um Chapter associado a um Group Chapter – Womens in Engineering (WiE).
				</span>
				<span v-else>Formed by more than <strong>60 members</strong>, all with a passion for sharing their knowledge and inspiring the next generation, our team is divided into 3 Chapters associated with Societies - Engineering in Medicine and Biology Society ( EMBS), Industry and Automation Society (IAS) and Computer Society (CS), and in a Chapter associated with a Group Chapter - Womens in Engineering (WiE).
				</span>
			</p>
			<p>&nbsp;</p>

			<h1 class='m-about-title'>
				<strong><span>IEEE</span></strong>
			</h1>
			<p>&nbsp;</p>
			<p class='m-about-text'>
				<span v-if="lang==='pt'">O IEEE (Institute of Electrical and Electronics Engineers), é a <strong>maior organização de profissionais técnicos</strong> dedicados ao avanço da Tecnologia para o benefício da Humanidade. Os seus membros inspiram a comunidade global a inovar com o objetivo de alcançar um futuro melhor, e concretizando-o através dos seus mais de <strong>423 000 membros</strong> oriundos de mais de <strong>160 países</strong>.
				</span>
				<span v-else>The IEEE (Institute of Electrical and Electronics Engineers), is the <strong> largest organization of technical professionals </strong> dedicated to the advancement of Technology for the benefit of Humanity. Its members inspire the global community to innovate with the aim of achieving a better future, and making it happen through its more than <strong> 423 000 members </strong> from more than <strong> 160 countries </strong> .
				</span>
			</p>
			<p class='m-about-text'>
				<span v-if="lang==='pt'">Como definido na sua declaração de visão, o IEEE procura ser essencial para a comunidade técnica global e para a todos os profissionais técnicos em todo o mundo, e ainda tem por objetivo ser universalmente reconhecido pelas suas contribuições na tecnologia, assim como no melhoramento das condições globais para os técnicos profissionais. O IEEE é ainda suportado por mais de 40 sociedades, que vão desde a Sociedade para a Engenharia Aplicada à Medicina e à Biologia, até a Sociedade da Ciência de Computadores, que implementam a visão do IEEE através dos diversos campos que abrangem a Engenharia Eletrotécnica e Electrónica, e as suas aplicações.
				</span>
				<span v-else>As defined in its vision statement, the IEEE seeks to be essential for the global technical community and for all technical professionals worldwide, and still aims to be universally recognized for its contributions in technology, as well as in improving conditions for professional technicians. The IEEE is also supported by more than 40 societies, ranging from the Society for Engineering Applied to Medicine and Biology, to the Computer Science Society, which implement the IEEE vision through the various fields that encompass Electrical Engineering and Electronics, and their applications.
				</span>
			</p>
		</div>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong>
				<span v-if="lang==='pt'">Eventos</span>
				<span v-else>Events</span>
			</strong>
		</h1>
		<p>&nbsp;</p>

		<events-carousel :events="events"/>

	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import BranchApi from '../api/BranchApi.ts';

	import EventsCarousel from '../components/EventsCarousel.vue';

 	@Component({ components: { 'events-carousel': EventsCarousel, }, })
	export default class HomeView extends Vue {

		public lang: string = this.$store.getters.getLang;

		public events: Event[] = [];

		public unwatch;

		public async created() {
			this.unwatch = this.$store.watch(
				(state, getters) => getters.getLang,
				(newValue, oldValue) => {
					this.lang = newValue;
				},
			);

			try {
				this.events = (await BranchApi.get_branch_events(this.lang)).reverse();
			} catch(error) {
				alert(error);
			}
		}

		public beforeDestroy() {
			this.unwatch();
		}

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