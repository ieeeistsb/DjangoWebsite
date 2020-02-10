<template>
	<div>
		<h1>Page Not Found</h1>

		<img id='homer-img' src='/static/public/assets/imgs/homer404.jpg'>

		<img id='paper-img' src='/static/public/assets/imgs/paper404.jpg'>

		<button class='btn btn-primary' @click="moveTo('/home')">Home Page</button>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component } from 'vue-property-decorator';

	@Component({})
	export default class NotFoundView extends Vue {

		public moveTo(path: string) {

			this.$router.push(path)
				.catch((err) => { /* Ignore */ });
		}

 	}
</script>

<style scoped>
	
	#homer-img {
		float: left;
	}

	#paper-img {
		float: right;
	}
</style>