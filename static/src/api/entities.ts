export interface App {
	device: string;
	lang: string;
}

export interface Community {
	name: string;
	tag: string;
	description ?: string[];
	events ?: Event[];
	members ?: Member[];
	pages: Page[];
}

export interface Event {
	name: string;
	description ?: string[];
}

export interface Member {
	name: string;
	social_media ?: string[];
}

export interface Page {
	name: string;
	type: string;
}
