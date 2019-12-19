<template>
	<div>
		<site-header/>

		<router-view/>

		<!--footer-->
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import Header from '../components/Header.vue';

	@Component({ components: { 'site-header': Header, }, })
	export default class PageLayout extends Vue {

	}
</script>

<style scoped>
	
</style>