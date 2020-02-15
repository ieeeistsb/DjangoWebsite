<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Eventos</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span>O departamento de eventos tem como função realizar desde momentos lúdicos, que visam proporcionar espaços de descontração aos estudantes do IST, até workshops, que visam ajudar os alunos a melhorar as suas skills técnicas. Os eventos organizados são pensados tendo em conta as necessidades dos alunos.
			</span>
		</p>

		<p>&nbsp;</p>

		<div v-for='event in getEvents()' class='m-event'>

			<event-card :event='event' />

		</div>

		<p>&nbsp;</p>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import EventCard from '../components/EventCard.vue';

	import { Event } from '../api/entities.ts';

	import CommunityModule from '../api/store/modules/community.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	@Component({ components: { 'event-card': EventCard, }, })
	export default class EventsView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public getEvents() {

			const community_module = new CommunityModule(this.tag);

			return community_module.events;

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

	.m-event {
		margin-left: 10%;
		margin-right: 10%;
	}

</style>