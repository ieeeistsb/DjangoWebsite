import Vue from 'vue';
import VueRouter from 'vue-router';
// @ts-ignore
import { constantRouterMap } from './config/router.config.ts';

import NProgress from 'nprogress'; // progress bar
import 'nprogress/nprogress.css'; // progress bar style

// @ts-ignore
import AppModule from './api/store/modules/app.ts';

// @ts-ignore
import { getStore } from './api/store/handler.ts';

NProgress.configure({ showSpinner: false }); // NProgress Configuration

const whiteList = ['home']; // no redirect whitelist

Vue.use(VueRouter);

const router = new VueRouter({
	/*mode: 'history',*/
	base: '',
	routes: constantRouterMap,
});

router.beforeEach((to, from, next) => {

	NProgress.start(); // start progress bar

	//if (to.fullPath.includes('community')) {
	//	if (!getStore('app') || !getStore('app').activeCommunity || !to.params.tag)
	//		next('/home');
	//}

	next();

});

router.afterEach(() => {
	NProgress.done(); // finish progress bar
});

export default router;
