<template>

		<div class="image-flip" ontouchstart="this.classList.toggle('hover');">

			<div class="mainflip">
				<div class="frontside">
					<div class="card">
						<div class="card-body text-center">
							<p><img class=" img-fluid" :src="member.image" alt="card image"></p>
							<h4 class="card-title">{{member.name}}</h4>
							<p class="card-text">{{member.role}}</p>
							<a href="#" class="btn btn-primary btn-sm"><i class="fa fa-plus"></i></a>
						</div>
					</div>
				</div>

				<div class="backside">
					<div class="card">
						<div class="card-body text-center mt-4">
							<h4 class="card-title">{{member.name}}</h4>
							<p class="card-text">{{member.description}}</p>
							<ul class="list-inline">
								<li class="list-inline-item">
									<a class="social-icon text-xs-center" target="_blank" :href="member.linkedin">
										<i class="fab fa-linkedin"></i>
									</a>
								</li>
								<li class="list-inline-item">
									<a class="social-icon text-xs-center" target="_blank" :href="'mailto:' + member.mail">
										<i class="fas fa-envelope mr-3"></i>
									</a>
								</li>
							</ul>
						</div>
					</div>
				</div>
			
			</div>
		</div>

</template>

<script lang='ts'>

	import { Vue, Component, Prop } from 'vue-property-decorator';

	import { Member } from '../api/entities.ts';

	@Component({})
	export default class MemberCard extends Vue {

		@Prop({ required: true, })
		public member : Member;

	}

</script>

<style scoped>
	
	.btn-primary:hover,
	.btn-primary:focus {
	    background-color: #108d6f;
	    border-color: #108d6f;
	    box-shadow: none;
	    outline: none;
	}

	.btn-primary {
	    color: #fff;
	    background-color: #007b5e;
	    border-color: #007b5e;
	}

	.card {
	    border: none;
	    background: #ffffff;
	}

	.image-flip:hover .backside,
	.image-flip.hover .backside {
	    -webkit-transform: rotateY(0deg);
	    -moz-transform: rotateY(0deg);
	    -o-transform: rotateY(0deg);
	    -ms-transform: rotateY(0deg);
	    transform: rotateY(0deg);
	    border-radius: .25rem;
	}

	.image-flip:hover .frontside,
	.image-flip.hover .frontside {
	    -webkit-transform: rotateY(180deg);
	    -moz-transform: rotateY(180deg);
	    -o-transform: rotateY(180deg);
	    transform: rotateY(180deg);
	}

	.mainflip {
	    -webkit-transition: 1s;
	    -webkit-transform-style: preserve-3d;
	    -ms-transition: 1s;
	    -moz-transition: 1s;
	    -moz-transform: perspective(1000px);
	    -moz-transform-style: preserve-3d;
	    -ms-transform-style: preserve-3d;
	    transition: 1s;
	    transform-style: preserve-3d;
	    position: relative;
	}

	.frontside {
	    position: relative;
	    -webkit-transform: rotateY(0deg);
	    -ms-transform: rotateY(0deg);
	    z-index: 2;
	    margin-bottom: 30px;
	}

	.backside {
	    position: absolute;
	    top: 0;
	    left: 0;
	    background: white;
	    -webkit-transform: rotateY(-180deg);
	    -moz-transform: rotateY(-180deg);
	    -o-transform: rotateY(-180deg);
	    -ms-transform: rotateY(-180deg);
	    transform: rotateY(-180deg);
	    -webkit-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
	    -moz-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
	    box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
	}

	.frontside,
	.backside {
		width: 100%;
	    -webkit-backface-visibility: hidden;
	    -moz-backface-visibility: hidden;
	    -ms-backface-visibility: hidden;
	    backface-visibility: hidden;
	    -webkit-transition: 1s;
	    -webkit-transform-style: preserve-3d;
	    -moz-transition: 1s;
	    -moz-transform-style: preserve-3d;
	    -o-transition: 1s;
	    -o-transform-style: preserve-3d;
	    -ms-transition: 1s;
	    -ms-transform-style: preserve-3d;
	    transition: 1s;
	    transform-style: preserve-3d;
	}

	.frontside .card,
	.backside .card {
	    min-height: 312px;
	}

	.backside .card a {
	    font-size: 18px;
	    color: #007b5e !important;
	}

	.frontside .card .card-title,
	.backside .card .card-title {
	    color: #007b5e !important;
	}

	.backside .card .card-text {
		height: 150px;
		overflow-y: scroll;
		overflow-x: hidden;
		text-align: justify;
	}

	.frontside .card .card-body img {
	    width: 120px;
	    height: 120px;
	    border-radius: 50%;
	}

</style>