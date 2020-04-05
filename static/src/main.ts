import Vue from 'vue';
import App from './App.vue';

// @ts-ignore
import router from './router.ts';

// @ts-ignore
import store from './store.ts';

// @ts-ignore
import Initializer from './config/bootstrap.ts';

// import './permission.ts'; // permission control

new Vue({
	router,
	store,
	beforeCreate() {
		Initializer();
	},
	render: (h) => h(App),
}).$mount('#app');
