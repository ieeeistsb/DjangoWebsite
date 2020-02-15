// @ts-ignore
import { ApiBase, Options } from './ApiBase.ts';

// @ts-ignore
import { environment } from './environments.ts';

// @ts-ignore
import { Community } from './entities.ts';

// @ts-ignore
import GetCommunitiesIO from './io/GetCommunitiesIO.ts';

// @ts-ignore
import GetCommunityEventsIO from './io/GetCommunityEventsIO.ts';

export default class CommunityApi extends ApiBase {

	private static readonly URL_BASE : string = environment.api_url + environment.api_version;

	public constructor() {
		super(CommunityApi.URL_BASE);
	}

	public static async get_communities(): Promise<any> {

		const io_handler : GetCommunitiesIO = new GetCommunitiesIO();

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_list_endpoint,
			parameters: io_handler.requestSerializer('pt'),
		} as Options<string>);

		return new Promise<any>((resolve, reject) => {

			promise.then((resp) => {
					const data = JSON.parse(JSON.stringify(resp.data));
					if (data) {
						resolve(io_handler.responseSerializer(data));
					}
				})
				.catch((err) => {
					reject(io_handler.errorSerializer(err));
				})
		});
	}

	public static async get_community_events(community_tag: string): Promise<any> {

		const io_handler : GetCommunityEventsIO = new GetCommunityEventsIO();

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_events_list_endpoint,
			parameters: io_handler.requestSerializer('pt', community_tag),
		} as Options<string>);

		return new Promise<any>((resolve, reject) => {

			promise.then((resp) => {
					const data = JSON.parse(JSON.stringify(resp.data));
					if (data) {
						resolve(io_handler.responseSerializer(data));
					}
				})
				.catch((err) => {
					reject(io_handler.errorSerializer(err));
				})
		});
	}

}
