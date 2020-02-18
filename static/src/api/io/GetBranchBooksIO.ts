// @ts-ignore
import { Book } from '../entities.ts';

export default class GetCommunitiesIO {

	public requestSerializer(lang: string) {
		return '?lang=' + lang;
	}

	public responseSerializer(data) {

		const books_list : Book[] = [];

		data.branch_books.forEach((book) => {
			books_list.push({
				'title' : book.title,
				'author' : book.author,
				'year_edition' : book.year_edition,
				'price' : book.price,
				'quality': book.quality,
				'contact' : book.contact,
				'img' : book.image
			} as Book);
		});

		return books_list;
	}

	public errorSerializer(error) {
		return error;
	}
}
