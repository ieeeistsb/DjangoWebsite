
// @ts-ignore
import { App, Community } from '../api/entities.ts';

// @ts-ignore
import app from '../api/store/modules/app.ts';

// @ts-ignore
import communities from '../api/store/modules/communities.ts';

// @ts-ignore
import config from './defaultSettings.ts';

export default function Initializer() {

	if (sessionStorage.getItem('app')) {

		app.setApp(JSON.parse(sessionStorage.getItem('app')));

	} else {

		const defaultApp: App = {
			device: config.device,
			lang: config.lang,
			active_community: config.active_community,
		};

		sessionStorage.setItem('app', JSON.stringify(defaultApp));

		app.setApp(defaultApp);

	}

	console.debug('App initialized');

	const defaultCommunities: Community[] = [];

	sessionStorage.setItem('communities', JSON.stringify(defaultCommunities));

	console.debug('Communities initialized');

}
