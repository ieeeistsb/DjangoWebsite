export interface Community {
	name: string;
	tag: string;
	pages: Page[];
}

export interface Page {
	name: string;
	type: string;
}