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

	import CommunityModule from '../api/store/modules/community.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	@Component({ components: {'site-header': Header, 'site-footer': Footer}, })
	export default class PageLayout extends Vue {

		public communities: Community[] = [];

		public beforeMount() {

			CommunityApi.get_communities()
				.then((resp) => {
					
					this.communities = resp;

					this.communities.forEach((community) => {
						CommunityModule.addCommunity(community);
					});
					
				})
				.catch((err) => console.error(err));
		}

	}
</script>

<style scoped>
	
</style>