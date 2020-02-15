<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>{{getTitle()}}</span></strong>
		</h1>
		<p>&nbsp;</p>

		<router-view/>
	
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';

	import CommunityModule from '../api/store/modules/community.ts';

	@Component({})
	export default class CommunityView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public getTitle() {

			const community_module = new CommunityModule(this.tag);

			return community_module.name + ' (' + this.tag + ')';
		}
	}
</script>

<style scoped>

	.m-about-title {
		text-align: center;
		color: #808080;
	}
	
</style>
