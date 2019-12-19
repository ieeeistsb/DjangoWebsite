<template>
	<div id="footer">
		<footer class="footer-responsive">

			<div class="footer-left">
				<h2> Onde Estamos </h2>
				<h3> Alameda </h3>
				<p> Av. Rovisco Pais, 1 <br> 1049-001 Lisboa <br> Portugal </p>
				<iframe width="250" height="250" id="gmap_canvas" src="https://maps.google.com/maps?q=Av.%20Rovisco%20Pais%2C%201%201049-001%20Lisboa%2CPortugal&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
			</div>

			<div class="footer-center">
				<h2 color ="transparent"> Onde Estamos</h2>
				<h3> Taguspark </h3>
				<p> Av. Prof. Doutor Cavaco Silva,<br> 2744-016 Porto Salvo<br> Portugal </p>
				<iframe width="250" height="250" id="gmap_canvas" src="https://maps.google.com/maps?q=Parque%20Taguspark%20D%2C%20Porto%20Salvo&t=&z=15&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
			</div>

			<div class="footer-right">
				<h2> Entra em Contacto </h2>
				<p> <img src="../assets/icons/phone-receiver.png" alt="phone-icon" width="12px"/> +351 21 423 3551<br> <img src="../assets/icons/close-envelope.png" alt="mail-icon" width="15px"/>  contact@ieee-ist.org</p>
				<p><a href="https://www.facebook.com/ieeeist"> <img src="../assets/icons/facebook.png" width="35px" padding="5em"/></a> <a href="https://www.instagram.com/ieee_ist/"> <img src="../assets/icons/instagram-512.png" width="35px"/> </a> <a href="https://www.linkedin.com/company/ieee-ist-student-branch/about/"> <img src="../assets/icons/linkedin-512.png" width="35px" padding="5m"/></a>  <a href="https://twitter.com/ieeeist"> <img src="../assets/icons/twitter.png" width="35px"/></a> </p>
				<div class="copyright">	
					<img src="../assets/logos/IST_A_RGB_NEG.png" alt="ist-icon" width="250px"/>
					<!-- Automatic site date update, 2019- current year -->
					<p> &copy;{{year}}, IEEE-IST SB </p>
				</div>
			</div>
		</footer>
	</div>
</template>

<script lang='ts'>
	import { Vue, Component, Prop } from 'vue-property-decorator';
  
  @Component({})
  export default class Footer extends Vue {
	public date: Date = new Date();
	public year: number = this.date.getFullYear();
  }
</script>

<style scoped>
	.mapouter {
		position:relative;
		text-align:right;
		height:250px;
		width:250px;
	}
	
	.gmap_canvas {
		overflow:hidden;
		background:none!important;
		height:250px;
		width:250px;
	}
</style>
