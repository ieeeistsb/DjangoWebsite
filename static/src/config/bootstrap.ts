
// @ts-ignore
import { App, Branch, Community } from '../api/entities.ts';

// @ts-ignore
import AppModule from '../api/store/modules/app.ts';

// @ts-ignore
import BranchModule from '../api/store/modules/branch.ts';

// @ts-ignore
import BranchApi from '../api/BranchApi.ts';

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

	const branch_module = new BranchModule();

	const defaultBranch: Branch = {
		name: 'IST Student Branch',
		tag: 'IST',
		description: []
	};

	branch_module.setBranch(defaultBranch);

	BranchApi.get_branch_books()
		.then((resp) => {

			branch_module.addBooks(resp);

		})
		.catch((err) => console.error(err));

}
