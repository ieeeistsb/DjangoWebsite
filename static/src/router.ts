import Vue from 'vue';
import VueRouter from 'vue-router';
// @ts-ignore
import { constantRouterMap } from './config/router.config.ts';

import NProgress from 'nprogress'; // progress bar
import 'nprogress/nprogress.css'; // progress bar style

// @ts-ignore
import { getStore } from './api/storage/handler.ts';

NProgress.configure({ showSpinner: true, }); // NProgress Configuration

const whiteList = ['home']; // no redirect whitelist

Vue.use(VueRouter);

const router = new VueRouter({
	/*mode: 'history',*/
	base: '',
	routes: constantRouterMap,
	scrollBehavior(to, from, savedPosition) { return { x: 0, y: 0 }; },
});

router.beforeEach((to, from, next) => {

	NProgress.start(); // start progress bar

	if (to.fullPath.includes('community')) {

		if (!getStore(to.params.tag)) {

			next('/404');

		}

	}

	next();

});

router.afterEach(() => {
	NProgress.done(); // finish progress bar
});

export default router;
