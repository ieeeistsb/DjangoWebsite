// @ts-ignore
import { Branch } from '../entities.ts';

export default class GetBranchIO {

	public requestSerializer(lang: string) {
		return '?lang=' + lang;
	}

	public responseSerializer(data) {

		const branch : Branch = data.branch as Branch;

		return branch;
	}

	public errorSerializer(error) {
		return error;
	}
}
