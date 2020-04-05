const production: boolean = false;

export const environment = {

	api_version: '/api/v1',

	api_url: production ? 'https://ieee-ist.org/' : 'http://127.0.0.1:8000',

	branch_endpoint: '/branch/',

	branch_events_list_endpoint: '/branch/events/',

	branch_books_list_endpoint: '/branch/books/',

	community_endpoint: '/community/',

	communities_list_endpoint: '/communities/',

	communities_events_list_endpoint: '/community/events/',

};
