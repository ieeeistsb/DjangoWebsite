<template>
	<div id='header'>
		<nav class='navbar navbar-expand-sm navbar-fixed-top m-nav'>

			<img src='../assets/logos/ieeeist-logo.png' class='logo'>

			<ul class='navbar-nav'>
				<li class='nav-item dropdown' v-for='community in communities'>
					<a class='nav-link dropdown-toggle' data-toggle='dropdown' href='#'>
						{{community}}
					</a>
					<div class='dropdown-menu'>
						<a class='dropdown-item' href='#'>OLA</a>
						<a class='dropdown-item' href='#'>OLA</a>
						<a class='dropdown-item' href='#'>OLA</a>
					</div>
				</li>
			</ul>

		</nav>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';
  
	@Component({})
	export default class Header extends Vue {

		public communities: string[] = ['CS', 'IAS'];
	}
</script>

<style scoped>

	#header {
		background-color: #e6e6e6;
		color: #000000;
		cursor: default;
		height: 4em;
		left: 0;
		line-height: 4em;
		position: fixed;
		text-align: right;
		top: 0;
		width: 100%;
		z-index: 10001;
	}

	#header .m-nav {
		height: 100%;
	}

	#header .logo {
		width: 10%;
		display:block;
		height:100%;
		left: 0;
		margin: 0;
		padding: 0;
	}

</style>
