export interface App {
	device : string;
	lang   : string;
}

export interface Branch {
	name : string;
	tag  : string;
	description ?: string[];
	books ?: Book[];
	members ?: Member[];
	events ?: Event[]; 
}

export interface Community {
	name  : string;
	tag   : string;
	description ?: string[];
	events  ?: Event[];
	members ?: Member[];
	pages : Page[];
}

export interface Event {
	name : string;
	date : string;
	description : string[];
	img  : string;
}

export interface Member {
	name : string;
	social_media ?: string[];
}

export interface Page {
	name : string;
	type : string;
}

export interface Book {
	title: string;
	author: string;
	year_edition: string;
	price: string;
	quality: string;
	contact: string;
	img: string;
}
