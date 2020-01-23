<template>
  <div>
  	<p>&nbsp;</p>
	<h1 class='m-about-title'>
		<strong><span>Computer Society (CS)</span></strong>
	</h1>
	<p>&nbsp;</p>

	<router-view/>
  	
  </div>
</template>

<script lang='ts'>
 	import { Vue, Component } from 'vue-property-decorator';

	@Component({})
	export default class CommunityView extends Vue {

	}
</script>

<style scoped>

	.m-about-title {
		text-align: center;
		color: #808080;
	}
	
</style>