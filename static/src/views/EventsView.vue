<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>{{lang==='pt' ? 'Eventos' : 'Events'}}</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span v-if="lang==='pt'">O departamento de eventos tem como função realizar desde momentos lúdicos, que visam proporcionar espaços de descontração aos estudantes do IST, até workshops, que visam ajudar os alunos a melhorar as suas skills técnicas. Os eventos organizados são pensados tendo em conta as necessidades dos alunos.
			</span>
			<span v-else>The function of the events department is to carry out from playful moments, which aim to provide relaxation spaces for IST students, to workshops, which aim to help students improve their technical skills. Organized events are designed with students' needs in mind.
			</span>
		</p>

		<p>&nbsp;</p>

		<div v-for='event in events' class='m-event'>

			<event-card :event='event' />

		</div>

		<p>&nbsp;</p>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import EventCard from '../components/EventCard.vue';

	import { Event } from '../api/entities.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	@Component({ components: { 'event-card': EventCard, }, })
	export default class EventsView extends Vue {

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