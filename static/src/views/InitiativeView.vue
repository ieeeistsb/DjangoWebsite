<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>{{initiative.name}}</span></strong>
		</h1>
		<p>&nbsp;</p>

		<!--IMAGE-->

		<p>&nbsp;</p>

		<!--DESCRIPTION-->

		<p>&nbsp;</p>

		<!--PROJECTS-->

		<p>&nbsp;</p>

		<!--TESTEMUNHAS-->

		<p>&nbsp;</p>

		<!--FAQ-->

		<p>&nbsp;</p>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import { Initiative } from '../api/entities.ts';

	@Component({ components: { 'event-card': EventCard, }, })
	export default class InitiativeView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		@Prop({ required: true, })
		public initiative: Initiative;

		public lang: string = this.$store.getters.getLang;

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