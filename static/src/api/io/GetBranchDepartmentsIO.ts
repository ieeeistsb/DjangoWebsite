// @ts-ignore
import { Department, Member } from '../entities.ts';

export default class GetBranchDepartmentsIO {

	public requestSerializer(lang: string) {
		return '?lang=' + lang;
	}

	public responseSerializer(data) {

		const events_list : Department[] = [];

		data.branch_departments.forEach((department) => {

			let members_list : Member[] = []

			department.members.forEach((member) => {
				members_list.push({
					'name': member.name,
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
