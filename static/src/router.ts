import Vue from 'vue';
import VueRouter from 'vue-router';
// @ts-ignore
import { constantRouterMap } from './config/router.config.ts';

Vue.use(VueRouter);

const router = new VueRouter({
    /*mode: 'history',*/
    base: '',
    routes: constantRouterMap,
});

export default router;
