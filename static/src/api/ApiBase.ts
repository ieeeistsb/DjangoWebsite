import axios from 'axios';

export interface Options<T> {
	endpoint: string;
	parameters: T;
}

export abstract class ApiBase {
	private readonly _urlBase: string;

	protected constructor(urlBase: string) {
		this._urlBase = urlBase;
	}

	protected static async doList<T>(options: Options<T>): Promise<any> {
		return axios({
			method: 'GET',
			url: options.endpoint + options.parameters,
		});
	}
}
