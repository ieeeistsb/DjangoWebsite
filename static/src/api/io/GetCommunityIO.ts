// @ts-ignore
import { Community } from '../entities.ts';

export default class GetCommunityIO {

	public requestSerializer(lang: string, community_tag: string) {
		return '?community=' + community_tag + '&lang=' + lang;
	}

	public responseSerializer(data) {

		const community : Community = data.community as Community;

		return community;
	}

	public errorSerializer(error) {
		return error;
	}
}
