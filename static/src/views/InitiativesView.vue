<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>{{lang==='pt' ? 'Iniciativas' : 'Initiatives'}}</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span v-if="lang==='pt'">Dentro da comunidade temos também várias iniciativas.
			</span>
			<span v-else>Within the community we also have several initiatives.
			</span>
		</p>

		<p>&nbsp;</p>

		<div v-for='initiative in initiatives' class='m-initiative'>

			<div>Initiative Title</div>

		</div>

		<p>&nbsp;</p>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import { Initiative } from '../api/entities.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	@Component({ components: { 'event-card': EventCard, }, })
	export default class InitiativesView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public lang: string = this.$store.getters.getLang;

		public initiatives: Initiative[] = [];

		async created() {
			try {
				// this.initiatives = (await CommunityApi.get_community_initiatives(this.tag, this.lang)).reverse();
			} catch(error) {
				alert(error);
			}
		}

		@Watch('tag')
		public async onTagUpdate(value, oldValue) {
			try {
				// this.initiatives = (await CommunityApi.get_community_initiatives(this.tag, this.lang)).reverse();
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

	.m-initiative {
		margin-left: 10%;
		margin-right: 10%;
	}

</style>