<template>
	<div>
		asdasda
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
	export default class EventCard extends Vue {

		@Prop({required: true,})
		public event : Event;

	}

</script>

<style scoped>
	
</style>
