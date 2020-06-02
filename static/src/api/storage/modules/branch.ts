
// @ts-ignore
import { setStore, getStore, } from '../handler.ts';

// @ts-ignore
import { Branch, Book, } from '../../entities.ts';

export default class BranchModule {

	private _branch: Branch | null = null;

	public constructor() {
		this._branch = getStore('IST');
	}

	public static setBranch(branch: Branch) { setStore(branch.tag, JSON.stringify(branch)); }

	public get branch() : Branch { return this._branch; }
	
	public get name()   : string         { return this._branch.name; }
	public get tag()    : string         { return this._branch.tag; }
	public get images() : string[]       { return this._branch.images; }
	public get books()  : Book[]         { return this._branch.books; }

	public setBranch(branch: Branch) { this._branch = branch; setStore(branch.tag, JSON.stringify(this._branch)); }

	public addBooks(books: Book[]) { this._branch.books = books; setStore(this._branch.tag, JSON.stringify(this._branch)); }
}
