
// @ts-ignore
import { App, Community } from '../api/entities.ts';

// @ts-ignore
import AppModule from '../api/store/modules/app.ts';

// @ts-ignore
import config from './defaultSettings.ts';

export default function Initializer() {

	const app_module = new AppModule();

	const defaultApp: App = {
		device: config.device,
		lang: config.lang,
		active_community: config.active_community,
	};

	app_module.setApp(defaultApp);

	console.debug('App initialized');

}
