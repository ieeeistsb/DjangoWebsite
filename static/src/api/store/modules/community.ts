
// @ts-ignore
import { setStore, getStore, } from '../handler.ts';

// @ts-ignore
import { Community, Event, Page, } from '../../entities.ts';

export default class CommunityModule {

	private _community: Community | null = null;

	public constructor(tag: string) {
		this._community = getStore(tag);
	}

	public static addCommunity(community: Community) { setStore(community.tag, JSON.stringify(community), 500); }

	public get community() : Community { return this._community; }

	public get name()   : string         { return this._community.name; }
	public get description() : string[]  { return this._community.description; }
	public get pages()  : Page[]         { return this._community.pages; }
	public get tag()    : string         { return this._community.tag; }
	public get events() : Event[]        { return this._community.events; }

	public setCommunity(community: Community) { this._community = community; setStore(community.tag, JSON.stringify(this._community), 500); }

	public addEvents(events: Event[]) { this._community.events = events; setStore(this._community.tag, JSON.stringify(this._community), 500); }
}
