<template>
	<div class="card m-news-card">

		<img v-bind:src="news.img" class="card-img-top" alt="...">

		<div class="card-body">

			<p class="card-text">{{news.title}}</p>

		</div>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import { News } from '../api/entities.ts';

	@Component({})
	export default class EventCard extends Vue {

		@Prop({ required: true, })
		public news : News;

		public lang: string = this.$store.getters.getLang;

	}

</script>

<style scoped>
	.m-news-card {
		width: 100%;
	}
</style>
