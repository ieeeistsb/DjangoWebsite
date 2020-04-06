<template>
	<div id='header' class='sticky-top'>
		<nav class='navbar navbar-expand-sm m-nav'>

			<button class='navbar-toggler' data-toggle='collapse' data-target='#collapse_target'>
				<span class='navbar-toggler-icon'><img class='m-collapse-icon' src='../assets/icons/collapse.png'></span>
			</button>

			<a class='navbar-brand logo' @click="moveTo('/home')"><img src='../assets/logos/ieee-ist-logo.png' class='logo-img'></a>

			<div class='collapse navbar-collapse navbar-button' id='collapse_target'>

				<ul class='navbar-nav m-nav-list ml-auto'>
					<li class='nav-item dropdown' v-for='community in communities'>
						<a class='nav-link dropdown-toggle m-community-title' data-toggle='dropdown' @click='moveToCommunity(community.tag, null)'>
							{{community.tag}}
						</a>
						<div class='dropdown-menu'>
							<a class='dropdown-item' v-for='page in community.pages' @click='moveToCommunity(community.tag, page.type)'>{{page.name}}</a>
						</div>
					</li>

					<li class='nav-item'>
						<a class='nav-link m-community-title' @click="moveTo('/team')">
							{{lang==='pt' ? 'Equipa' : 'Team'}}
						</a>
					</li>

					<li class='nav-item'>
						<a class='nav-link m-community-title' @click='toggleLang()'>
							{{lang}}
						</a>
					</li>

				</ul>

			</div>

		</nav>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import { clearAll } from '../api/storage/handler.ts';

	import CommunityModule from '../api/storage/modules/community.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	import { Community } from '../api/entities.ts';
  
	@Component({})
	export default class Header extends Vue {

		@Prop({ required: true, })
		public communities: Community[] = [];

		public lang: string = this.$store.getters.getLang;

		public moveTo(path: string) {

			this.$router.push(path)
				.catch((err) => { /* Ignore */ });
		}

		public moveToCommunity(tag: string, type: string) {

			let toPath;

			if (type) {

				toPath = '/community/' + tag + '/' + type;

			} else {
				
				toPath = '/community/' + tag;

			}

			this.$router.push({path: toPath, params: { tag: tag, }})
				.catch((err) => { /* Ignore */ });

		}

		public async toggleLang() {
			this.lang = this.lang === 'pt' ? 'en' : 'pt';
			clearAll();
			await this.$store.dispatch('lang', this.lang);
			this.$emit('langChanged');
			this.moveTo('/home');
		}

	}
</script>

<style scoped>

	#header {
		background-color: #e8e8e8;
		color: gray;
		width: 100%;
	}

	#header .m-nav {
		padding: 0;
	}

	.m-collapse-icon {
		width: 100%;
		height: 100%;
	}

	#header .logo {
		padding: 0;
		margin-left: 25px;
		cursor: pointer;
	}

	#header .logo-img {
		width: 150px;
		display:block;
		padding: 0;
	}

	.ml-auto .dropdown-menu {
    	left: auto !important;
    	right: 0px;
	}

	#header .m-community-title {
		color: gray;
		margin: 20px;
		cursor: pointer;
	}

	#header .m-community-title:hover {
		color: steelblue;
	}

	.dropdown:hover>.dropdown-menu {
 		display: block;
	}

</style>
