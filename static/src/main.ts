import Vue from 'vue';
import App from './App.vue';
// @ts-ignore
import router from './router.ts';

// import './permission.ts'; // permission control

new Vue({
	router,
	render: (h) => h(App),
}).$mount('#app');