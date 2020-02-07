import { VuexModule, Module, getModule, Mutation } from 'vuex-module-decorators';

// @ts-ignore
import store from '../index.ts';

// @ts-ignore
import { App } from '../../entities.ts';

@Module({
	namespaced: true,
	name: 'app',
	store,
	dynamic: true,
})
class AppModule extends VuexModule {
	private app: App | null = null;

	public get device(): string          { return this.app.device; }
	public get isDesktop(): boolean      { return this.app.device === 'desktop'; }
	public get lang(): string            { return this.app.lang; }
	public get activeCommunity(): string { return this.app.active_community; }

	@Mutation
	public setApp(app: App) { this.app = app; sessionStorage.setItem('app', JSON.stringify(this.app)); }

	@Mutation
	public toggleActiveCommunity(community: string) { this.app.active_community = community; sessionStorage.setItem('app', JSON.stringify(this.app)); }

	@Mutation
	public toggleDevice(device: string) { this.app.device = device; sessionStorage.setItem('app', JSON.stringify(this.app)); }

	@Mutation
	public toggleLang(lang: string) { this.app.lang = lang; sessionStorage.setItem('app', JSON.stringify(this.app)); }

}

export default getModule(AppModule);
