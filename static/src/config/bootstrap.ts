
// @ts-ignore
import { Branch } from '../api/entities.ts';

// @ts-ignore
import BranchModule from '../api/storage/modules/branch.ts';

// @ts-ignore
import BranchApi from '../api/BranchApi.ts';

export default function Initializer() {

	const branch_module = new BranchModule();

	const defaultBranch: Branch = {
		name: 'IST Student Branch',
		tag: 'IST',
		description: []
	};

	// const branch = (await BranchApi.get_branch()).reverse();

	branch_module.setBranch(defaultBranch);

}
