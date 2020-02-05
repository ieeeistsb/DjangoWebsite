// @ts-ignore
import { Community } from '../entities.ts';

export default class GetCommunitiesIO {

	public requestSerializer() {
		return '';
	}

	public responseSerializer(data) {

		const communities_list : Community[] = [];

		data.communities.forEach((community) => {
			communities_list.push({
				'name' : community.name,
				'tag' : community.tag,
				'pages': community.pages,
			} as Community);
		});

		return communities_list;
	}

	public errorSerializer(error) {
		return error;
	}
}