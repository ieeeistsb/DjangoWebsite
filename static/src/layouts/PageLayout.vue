<template>
	<div>
		<site-header/>

		<router-view/>

		<site-footer/>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import Header from '../components/Header.vue';
	import Footer from '../components/Footer.vue';

	@Component({ components: {'site-header': Header, 'site-footer': Footer}, })
	export default class PageLayout extends Vue {

	}
</script>

<style scoped>
	
</style>