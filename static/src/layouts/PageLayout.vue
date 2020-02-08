<template>
	<div>
		<site-header @switchCommunity='reloadCommunity'/>

		<router-view :community='community'/>

		<site-footer/>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import Header from '../components/Header.vue';
	import Footer from '../components/Footer.vue';

	import { Community } from '../api/entities.ts';

	import CommunityModule from '../api/store/modules/community.ts';

	import AppModule from '../api/store/modules/app.ts';

	@Component({ components: {'site-header': Header, 'site-footer': Footer}, })
	export default class PageLayout extends Vue {

		public community : Community;

		public reloadCommunity(tag: string) {
			const community_module = new CommunityModule(tag);
			this.community = community_module.community;
		}

	}
</script>

<style scoped>
	
</style>