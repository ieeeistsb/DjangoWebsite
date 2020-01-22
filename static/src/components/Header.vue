<template>
	<div id='header'>
		<nav class='navbar navbar-expand-sm navbar-fixed-top m-nav'>

			<button class='navbar-toggler' data-toggle='collapse' data-target='#collapse_target'>
				<span class='navbar-toggler-icon'><img class='m-collapse-icon' src='../assets/icons/collapse.png'></span>
			</button>

			<a class='navbar-brand logo'><img src='../assets/logos/ieee-ist-logo.png' class='logo-img'></a>

			<div class='collapse navbar-collapse navbar-button' id='collapse_target'>

				<ul class='navbar-nav m-nav-list ml-auto'>
					<li class='nav-item dropdown' v-for='community in communities'>
						<a class='nav-link dropdown-toggle m-community-title' data-toggle='dropdown' href='#'>
							{{community.name}}
						</a>
						<div class='dropdown-menu'>
							<a class='dropdown-item' v-for='topic in community.topics' href='#'>{{topic}}</a>
						</div>
					</li>
				</ul>

			</div>

		</nav>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	interface Community {
		name: string;
		topics: string[];
	}
  
	@Component({})
	export default class Header extends Vue {

		public communities: Community[] = [
			{'name': 'CS',   'topics': ['Membros', 'Eventos', 'Mais']},
			{'name': 'IAS',  'topics': ['Membros', 'Eventos']},
			{'name': 'EMBS', 'topics': ['Membros']},
			{'name': 'Wie',  'topics': ['Membros']}
		];

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
		margin: 15px;
	}

	#header .m-community-title:hover {
		color: steelblue;
	}

	.dropdown:hover>.dropdown-menu {
 		display: block;
	}

</style>
