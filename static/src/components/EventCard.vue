<template>
	<div class='card mb-3 m-event-card'>

		<div class='row no-gutters'>

			<div class='col-md-4'>

			<img v-bind:src="'/static/public/assets/cs/' + event.img" class='card-img'>

			</div>

			<div class='col-md-8'>

				<div class='card-body'>

					<h5 class='card-title'>{{event.name}}</h5>

					<p>
						<span class='card-text'>
							<strong>{{lang==='pt' ? 'Data' : 'Date'}}: </strong>{{event.date}}
						</span>
					</p>

					<p v-for='paragraph in event.description' class='card-text'>{{paragraph}}</p>

				</div>

			</div>

		</div>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import { Event } from '../api/entities.ts';

	@Component({})
	export default class EventCard extends Vue {

		@Prop({ required: true, })
		public event : Event;

		public lang: string = this.$store.getters.getLang;

	}

</script>

<style scoped>
	.m-event-card {
		width: 100%;
	}
</style>
