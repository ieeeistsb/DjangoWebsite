<template>
	<div>
		<site-header :communities='communities'/>

		<router-view/>

		<site-footer :communities='communities'/>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import Header from '../components/Header.vue';
	import Footer from '../components/Footer.vue';

	import { Community } from '../api/entities.ts';

	import CommunityModule from '../api/storage/modules/community.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	import BranchApi from '../api/BranchApi.ts';

	@Component({ components: {'site-header': Header, 'site-footer': Footer}, })
	export default class PageLayout extends Vue {

		public communities: Community[] = [];

		async created() {

			this.communities = (await CommunityApi.get_communities()).reverse();

			this.communities.forEach((community) => {
				CommunityModule.addCommunity(community);
			});

		}

	}
</script>

<style scoped>
	
</style>