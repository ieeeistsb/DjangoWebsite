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
		lang(state: State, new_lang: string) {
			state.lang = new_lang;
		}
	},
	actions: {
		lang({ commit }, new_lang) {
			commit('lang', new_lang);
		}
	},
	getters: {
		isDesktop(state: State): boolean {
			return state.device === 'desktop';
		},
		getDevice(state: State): string {
			return state.device;
		},
		getLang(state: State): string {
			return state.lang;
		}
	}
};

Vue.use(Vuex);

export default new Vuex.Store(store);