
// @ts-ignore
import { App, Community } from '../api/entities.ts';

// @ts-ignore
import AppModule from '../api/store/modules/app.ts';

// @ts-ignore
import CommunityModule from '../api/store/modules/community.ts';

// @ts-ignore
import CommunityApi from '../api/CommunityApi.ts';

// @ts-ignore
import config from './defaultSettings.ts';

export default function Initializer() {

	const app_module = new AppModule();

	const defaultApp: App = {
		device: config.device,
		lang: config.lang,
	};

	app_module.setApp(defaultApp);

}
