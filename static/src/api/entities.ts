export interface Branch {
	name : string;
	tag  : string;
	images ?: string[];
	description ?: string[];
	books ?: Book[];
	members ?: Member[];
	events ?: Event[]; 
}

export interface Community {
	name  : string;
	tag   : string;
	description ?: string[];
	images : string[];
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
	name: string;
	role: string;
	mail: string;
	linkedin: string;
	description: string;
	image: string;
}

export interface Department {
	name: string;
	members: Member[];
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
