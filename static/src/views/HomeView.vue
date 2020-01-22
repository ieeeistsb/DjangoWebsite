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

		<div id='eventsCarousel' class='carousel slide' data-ride='carousel'>
			
			<div class='carousel-inner'>
				<div v-bind:class="'carousel-item' + t[0].name == events.name ? ' active' :''" v-for='t in trio'>
					
					<div class='card m-events-card' v-for='event in t'>
						<img v-bind:src="'/static/public/assets/cs/' + event.img" class='card-img-top'>
						<div class='card-body'>
							<h5 class='card-title'>{{event.name}}</h5>
							<p class='card-text'>{{event.description}}</p>
							<a href='#' class='btn btn-primary'>Saber Mais</a>
						</div>
					</div>

				</div>

			</div>

		</div>

	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	interface Event {
		name: string;
		description: string;
		img: string;
	}

	@Component({})
	export default class HomeView extends Vue {

		public events: Event[] = [
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'}
		];

		public trio: Event[][] = [];

		public generateCarousel() {

			let n: number = 0;
			let c: number = 0;

			while(c < this.events.length) {
				this.trio.push([]);
				for (let i = 0; i < 3 && c < this.events.length; i++) {
					console.log(this.trio[n]);
					console.log(this.events[c]);
					this.trio[n].push(this.events[c++]);
				}
				n++;
			}

		}

		public beforeMount() {
			this.generateCarousel();
		}

	}
</script>

<style scoped>
	.home-img {
		width: 100%;
		height: auto;
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

	#eventsCarousel {
		height: 150px;
		margin-left: 10%;
		margin-right: 10%;
	}

	.m-events-img {
		width: 100%;
		height: 50px;
	}

	.m-events-card {
		width: 18rem;
		margin: 4%;
		display: inline-block;
	}
</style>