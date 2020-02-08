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
				path: 'community/:tag',
				component: CommunityView,
				meta: { title: 'Community'},
				redirect: '/community/:tag/about',
				children: [
					{
						path: 'about',
						component: AboutView,
						props: { name: 'community', },
						meta: { title: 'Community', type: 'about', },
					},
					{
						path: 'members',
						component: MembersView,
						meta: { title: 'Members', type: 'members', },
					},
					{
						path: 'events',
						component: EventsView,
						meta: { title: 'Events', type: 'events', },
					}
				]
			},
			{
				path: 'repository',
				component: RepositoryView,
				meta: { title: 'Repository', type: 'repository', },
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
		component: NotFoundView,
		meta: { title: 'Page Not Found', },
	}
];
