// @ts-ignore
import { PageLayout } from '../layouts/index.ts';

// @ts-ignore
import { NotFoundView, HomeView } from '../views/index.ts';

export const asyncRouterMap = [];


export const constantRouterMap = [
	{
		path: '',
		component: PageLayout,
		name: 'page_layout',
		meta: { title: 'IEEE-IST'},
		redirect: '/home',
		children: [
			{
				path: 'home',
				component: HomeView,
				meta: { title: 'Home'},
			},
		]
	},
	{
		path: '/404',
		name: 'http404',
		component: NotFoundView,
		meta: { title: 'Page Not Found', },
	}
];
