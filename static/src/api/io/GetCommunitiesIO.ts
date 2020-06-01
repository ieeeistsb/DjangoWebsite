// @ts-ignore
import { Community } from '../entities.ts';

export default class GetCommunitiesIO {

	public requestSerializer(lang: string) {
		return '?lang=' + lang;
	}

	public responseSerializer(data) {

		const communities_list : Community[] = [];

		data.communities.forEach((community) => {
			communities_list.push({
				'name' : community.name,
				'tag' : community.tag,
				'description' : community.description,
				'images' : community.images,
				'pages': community.pages,
			} as Community);
		});

		return communities_list;
	}

	public errorSerializer(error) {
		return error;
	}
}
