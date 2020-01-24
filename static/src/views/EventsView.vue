<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Eventos</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span>O departamento de Eventos é o mais recente na EMBS, tendo sido fundado em 2017 pela atual Chair, Maria Leonor Narciso, devido à necessidade crescente da existência duma secção especializada em organizar eventos. Como o nome indica, a função deste departamento é realizar o planeamento e concretização de eventos pontuais, como a noite de Quizz, ou recorrentes, como a Caixa de Pandora. Desde momentos lúdicos que visam proporcionar espaços de descontração aos estudantes do IST, até workshops que visam ajudar os alunos a melhorar as suas skills técnicas, os eventos organizados são pensados tendo em conta as necessidades dos alunos.
			</span>
		</p>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Iniciativas</span></strong>
		</h1>
		<p>&nbsp;</p>

		<div v-for='event in events'>

			<event-card :event='event' />

		</div>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>WorkShops</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span>Para além de todos os eventos descritos, a EMBS oferece-te também uma vasta panóplia de workshops, desde os mais técnicos como workshops de Python até aos mais lúdicos, que formam os estudantes tanto nas componentes académicas, como no âmbito das softskills.
			</span>
		</p>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component } from 'vue-property-decorator';

	import EventCard from '../components/EventCard.vue';

	interface Event {
		name: string;
		description: string;
		img: string;
	}

	@Component({ components: { 'event-card': EventCard, }, })
	export default class EventsView extends Vue {

		public events: Event[] = [
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'},
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'},
			{'name': 'Code Night', 'description': 'Vem acabar os projetos com companhia e diversão.', 'img': 'events.jpg'},
			{'name': 'Quantum Computing', 'description': 'Vem aprender a programar em computadores quanticos.', 'img': 'header.jpg'}
		];

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

</style>