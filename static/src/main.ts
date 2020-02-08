import Vue from 'vue';
import App from './App.vue';

// @ts-ignore
import router from './router.ts';

// @ts-ignore
import Initializer from './config/bootstrap.ts';

// import './permission.ts'; // permission control

new Vue({
	router,
	beforeCreate() {
		console.debug('Loading/Creating session storage Data');
		Initializer();
	},
	render: (h) => h(App),
}).$mount('#app');
