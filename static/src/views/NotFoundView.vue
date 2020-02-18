<template>
	<div>

		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<button class='btn btn-primary m-btn' @click="moveTo('/home')">Home Page</button>
		</h1>
		<p>&nbsp;</p>


		<div class='container'>
			<img class='m-img' src='/static/public/assets/imgs/notfound.jpg'>
		</div>

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
	.m-img {
		width: 100%;
	}

	.m-btn {
		left: 50%;
	}

	.m-about-title {
		text-align: center;
		color: #808080;
	}
</style>