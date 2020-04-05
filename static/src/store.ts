import Vue from 'vue';
import Vuex from 'vuex';

// @ts-ignore
import { App, Branch, Community } from '../../entities.ts';

interface State {
	device: string;
	lang: string;
}

const state: State = {
	device: "desktop",
	lang: "pt"
};

const store = {
	state: state,
	mutations: {
		setDevice(state: State, device: string) {
			state.device = device;
		},
		setLang(state: State, lang: string) {
			state.lang = lang;
		}
	},
	actions: {},
	getters: {
		isDesktop(state: State): boolean {
			return state.device === 'desktop';
		},
		getDevice(state: State): string {
			return state.device;
		},
		getLang(state: State): string {
			return  state.lang;
		}
	}
};

Vue.use(Vuex);

export default new Vuex.Store(store);