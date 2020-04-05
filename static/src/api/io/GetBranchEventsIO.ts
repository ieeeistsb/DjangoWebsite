// @ts-ignore
import { Event } from '../entities.ts';

export default class GetBranchEventsIO {

	public requestSerializer(lang: string) {
		return '?lang=' + lang;
	}

	public responseSerializer(data) {

		const events_list : Event[] = [];

		data.branch_events.forEach((event) => {
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
