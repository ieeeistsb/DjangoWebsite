// @ts-ignore
import { Event } from '../entities.ts';

export default class GetCommunitiesIO {

	public requestSerializer(lang: string, community_tag: string) {
		return '?community=' + community_tag + '&lang=' + lang;
	}

	public responseSerializer(data) {

		const events_list : Event[] = [];

		data.community_events.forEach((event) => {
			events_list.push({
				'name' : event.name,
				'date' : event.date,
				'description' : event.description,
				'img': event.image,
			} as Event);
		});

		return events_list;
	}

	public errorSerializer(error) {
		return error;
	}
}
