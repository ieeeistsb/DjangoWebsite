// @ts-ignore
import { ApiBase, Options } from './ApiBase.ts';

// @ts-ignore
import { environment } from './environments.ts';

// @ts-ignore
import { Branch, Book } from './entities.ts';

// @ts-ignore
import GetBranchIO from './io/GetBranchIO.ts';

// @ts-ignore
import GetBranchBooksIO from './io/GetBranchBooksIO.ts';

// @ts-ignore
import GetBranchEventsIO from './io/GetBranchEventsIO.ts';

//@ts-ignore
import GetBranchDepartmentsIO from './io/GetBranchDepartmentsIO.ts';


export default class BranchApi extends ApiBase {

	private static readonly URL_BASE : string = environment.api_url + environment.api_version;

	public constructor() {
		super(BranchApi.URL_BASE);
	}

	public static async get_branch(lang: string): Promise<any> {

		const io_handler : GetBranchIO = new GetBranchIO();

		const promise = super.doList<string>({
			endpoint: BranchApi.URL_BASE + environment.branch_endpoint,
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

	public static async get_branch_events(lang: string): Promise<any> {

		const io_handler : GetBranchEventsIO = new GetBranchEventsIO();

		const promise = super.doList<string>({
			endpoint: BranchApi.URL_BASE + environment.branch_events_list_endpoint,
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

	public static async get_branch_departments(lang: string): Promise<any> {

		const io_handler : GetBranchDepartmentsIO = new GetBranchDepartmentsIO();

		const promise = super.doList<string>({
			endpoint: BranchApi.URL_BASE + environment.branch_departments_list_endpoint,
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

	public static async get_branch_books(lang: string): Promise<any> {

		const io_handler : GetBranchBooksIO = new GetBranchBooksIO();

		const promise = super.doList<string>({
			endpoint: BranchApi.URL_BASE + environment.branch_books_list_endpoint,
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

}
