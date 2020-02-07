export interface App {
	device: string;
	lang: string;
	active_community: string;
}

export interface Community {
	name: string;
	tag: string;
	description ?: string;
	pages: Page[];
}

export interface Page {
	name: string;
	type: string;
}