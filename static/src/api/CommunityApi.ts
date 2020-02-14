// @ts-ignore
import { ApiBase, Options } from './ApiBase.ts';

// @ts-ignore
import { environment } from './environments.ts';

// @ts-ignore
import { Community } from './entities.ts';

// @ts-ignore
import GetCommunitiesIO from './io/GetCommunitiesIO.ts';


export default class CommunityApi extends ApiBase {

	private static readonly URL_BASE : string = environment.api_url + environment.api_version;

	private static io_handler : GetCommunitiesIO = new GetCommunitiesIO();

	public constructor() {
		super(CommunityApi.URL_BASE);
	}

	public static async get_communities(): Promise<any> {

		const promise = super.doList<string>({
			endpoint: CommunityApi.URL_BASE + environment.communities_list_endpoint,
			parameters: this.io_handler.requestSerializer('pt'),
		} as Options<string>);

		return new Promise<any>((resolve, reject) => {

			promise.then((resp) => {
					const data = JSON.parse(JSON.stringify(resp.data));
					if (data) {
						resolve(this.io_handler.responseSerializer(data));
					}
				})
				.catch((err) => {
					reject(this.io_handler.errorSerializer(err));
				})
		});
	}

}
