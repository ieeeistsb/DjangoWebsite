import router from './router';

// import NProgress from 'nprogress'; // progress bar
// import 'nprogress/nprogress.css'; // progress bar style
//import { setDocumentTitle, domTitle } from '@/utils/domUtil';

// NProgress.configure({ showSpinner: false }); // NProgress Configuration

const whiteList = ['home']; // no redirect whitelist

router.beforeEach((to, from, next) => {
	next('/home');
//   NProgress.start(); // start progress bar
//   if (to.meta && typeof to.meta.title !== undefined) {
//     setDocumentTitle(`${to.meta.title} - ${domTitle}`);
//   }
//   if (false) { // check if user is logged
//     if (to.path === '/user/login') {
//       next('/home');
//       NProgress.done();
//     } else {
//       next();
//     }
//   } else {
//     if (whiteList.includes(to.name)) {
//       next();
//     } else {
//       next('/home');
//       NProgress.done(); // if current page is login will not trigger afterEach hook, so manually handle it
//     }
//   }
});

// router.afterEach(() => {
//   NProgress.done(); // finish progress bar
// });
