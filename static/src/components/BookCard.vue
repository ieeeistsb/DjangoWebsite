<template>
	<div class='card mb-3 m-event-card'>

		<div class='row no-gutters'>

			<div class='col-md-4'>

			<img v-bind:src="'/static/public/assets/cs/' + book.img" class='card-img'>

			</div>

			<div class='col-md-8'>

				<div class='card-body'>

					<h5 class='card-title'>{{book.title}}</h5>

					<p>
						<strong>Autor: </strong>
						<span class='card-text'>{{book.author}}</span>
					</p>

					<p>
						<strong>Edição/Ano: </strong>
						<span class='card-text'>{{book.year_edition}}</span></p>

					<p>
						<strong>Preço: </strong>
						<span class='card-text'>{{book.price}}</span></p>

					<p>
						<strong>Estado: </strong>
						<span class='card-text'>{{book.quality}}</span>
					</p>

					<p>
						<strong>Contacto: </strong>
						<span class='card-text'>{{book.contact}}</span>
					</p>

				</div>

			</div>

		</div>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import { Book } from '../api/entities.ts';

	@Component({})
	export default class BookCard extends Vue {

		@Prop({ required: true, })
		public book : Book;

	}

</script>

<style scoped>
	
</style>
