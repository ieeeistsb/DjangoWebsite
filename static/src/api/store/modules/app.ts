
// @ts-ignore
import { setStore, getStore, } from '../handler.ts';

// @ts-ignore
import { App } from '../../entities.ts';

export default class AppModule {
	private app: App | null = getStore('app');

	public get device(): string          { return this.app.device; }
	public get isDesktop(): boolean      { return this.app.device === 'desktop'; }
	public get lang(): string            { return this.app.lang; }

	public setApp(app: App) { this.app = app; setStore('app', JSON.stringify(this.app)); }

	public toggleDevice(device: string) { this.app.device = device; setStore('app', JSON.stringify(this.app), 500); }

	public toggleLang(lang: string) { this.app.lang = lang; setStore('app', JSON.stringify(this.app), 500); }

}
