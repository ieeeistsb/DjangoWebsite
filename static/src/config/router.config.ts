// @ts-ignore
import { PageLayout } from '../layouts/index.ts';

// @ts-ignore
import { NotFoundView, HomeView, CommunityView, AboutView, TeamView, MembersView, EventsView, RepositoryView } from '../views/index.ts';

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
				path: 'community',
				component: CommunityView,
				meta: { title: 'Community'},
				redirect: '/community/about',
				children: [
					{
						path: 'about',
						component: AboutView,
						meta: { title: 'Community'},
					},
					{
						path: 'members',
						component: MembersView,
						meta: { title: 'Members'},
					},
				]
			},
			{
				path: 'repository',
				component: RepositoryView,
				meta: { title: 'Repository'},
			},
			{
				path: 'team',
				component: TeamView,
				meta: { title: 'Team'},
			}
		]
	},
	{
		path: '/404',
		name: 'http404',
		component: NotFoundView,
		meta: { title: 'Page Not Found', },
	}
];
