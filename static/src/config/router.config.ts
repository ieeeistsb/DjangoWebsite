// @ts-ignore
import { PageLayout } from '../layouts/index.ts';

// @ts-ignore
import { NotFoundView, HomeView, CommunityView, AboutView, TeamView, MembersView, EventsView, } from '../views/index.ts';

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
			{
				path: 'community/:tag',
				component: CommunityView,
				props: true,
				meta: { title: 'Community'},
				redirect: '/community/:tag/about',
				children: [
					{
						path: 'about',
						component: AboutView,
						props: true,
						meta: { title: 'Community', type: 'about', },
					},
					{
						path: 'members',
						component: MembersView,
						props: true,
						meta: { title: 'Members', type: 'members', },
					},
					{
						path: 'events',
						component: EventsView,
						props: true,
						meta: { title: 'Events', type: 'events', },
					},
				]
			},
			{
				path: 'team',
				component: TeamView,
				meta: { title: 'Team', type: 'team', },
			}
		]
	},
	{
		path: '*',
		name: 'http404',
		redirect: '/home',
		meta: { title: 'Page Not Found', },
	}
];
