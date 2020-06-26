// @ts-ignore
import { ApiBase, Options } from './ApiBase.ts';

// @ts-ignore
import { environment } from './environments.ts';

// @ts-ignore
import { Community } from './entities.ts';

// @ts-ignore
import GetCommunityIO from './io/GetCommunityIO.ts';

// @ts-ignore
import GetCommunitiesIO from './io/GetCommunitiesIO.ts';

// @ts-ignore
import GetCommunityEventsIO from './io/GetCommunityEventsIO.ts';

// @ts-ignore
import GetCommunityDepartmentsIO from './io/GetCommunityDepartmentsIO.ts';

export default class CommunityApi extends ApiBase {

	private static readonly URL_BASE : string = environment.api_url + environment.api_version;

	public constructor() {
		super(CommunityApi.URL_BASE);
	}

	public static async get_community(tag: string, lang: string): Promise<any> {

		const io_handler : GetCommunityIO = new GetCommunityIO();

		const promise = super.get<string>({
			endpoint: CommunityApi.URL_BASE + environment.community_endpoint,
			parameters: io_handler.requestSerializer(lang, tag),
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

	public static async get_communities(lang: string): Promise<any> {

		const io_handler : GetCommunitiesIO = new GetCommunitiesIO();

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_list_endpoint,
			parameters: io_handler.requestSerializer(lang),
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

	public static async get_community_events(community_tag: string, lang: string): Promise<any> {

		const io_handler : GetCommunityEventsIO = new GetCommunityEventsIO();

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_events_list_endpoint,
			parameters: io_handler.requestSerializer(lang, community_tag),
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

	public static async get_community_departments(community_tag: string, lang: string, scholarYear: string): Promise<any> {

		const io_handler : GetCommunityDepartmentsIO = new GetCommunityDepartmentsIO();

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_departments_list_endpoint,
			parameters: io_handler.requestSerializer(lang, community_tag, scholarYear),
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
