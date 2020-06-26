// @ts-ignore
import { Department, Member } from '../entities.ts';

export default class GetCommunityDepartmentsIO {

	public requestSerializer(lang: string, community_tag: string, scholar_year: string) {
		return '?community=' + community_tag + '&lang=' + lang + '&scholar_year=' + scholar_year;
	}

	public responseSerializer(data) {

		const events_list : Department[] = [];

		data.community_departments.forEach((department) => {

			let members_list : Member[] = []

			department.members.forEach((member) => {
				members_list.push({
					'name' : member.name,
					'role' : member.role,
					'mail' : member.mail,
					'linkedin' : member.linkedin,
					'description' : member.description,
					'image' : member.image
				} as Member);
			});

			events_list.push({
				'name' : department.name,
				'members' : members_list
			} as Department);
		});

		return events_list;
	}

	public errorSerializer(error) {
		return error;
	}
}
