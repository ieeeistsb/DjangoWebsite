import { VuexModule, Module, getModule, Mutation, Action } from 'vuex-module-decorators';

// @ts-ignore
import store from '../index.ts';

// @ts-ignore
import { Community } from '../../entities.ts';

@Module({
	namespaced: true,
	name: 'communities',
	store,
	dynamic: true,
})
class CommunityModule extends VuexModule {
	private communities: Community[] = [];

	public get getCommunities() : Community[] { return this.communities; }

	@Mutation
	public setCommunities(communities: Community[]) { this.communities = communities; sessionStorage.setItem('communities', JSON.stringify(this.communities)); }

	@Mutation
	public addCommunity(community) { this.communities.push(community); sessionStorage.setItem('communities', JSON.stringify(this.communities)); }

	@Action({})
	public getCommunity(tag: string) {
		this.communities.forEach((community) => {
			if (community.tag == tag) {
				return community;
			}
		});
	}

	@Action({})
	public hasCommunity(tag: string) {
		this.communities.forEach((community) => {
			if (community.tag == tag) {
				return true;
			}
		});
		return false;
	}

}

export default getModule(CommunityModule);
