<template>
	<div>
		asdasda
	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	interface Book {
		title: string;
		author: string;
		year_edition: string;
		price: string;
		quality: string;
		contact: string;
	}

	@Component({})
	export default class BookCard extends Vue {

		@Prop({required: true,})
		public book : Book;

	}

</script>

<style scoped>
	
</style>
