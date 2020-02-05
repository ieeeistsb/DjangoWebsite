<template>
	
	<!-- Footer -->
	<footer id='footer' class="page-footer pt-4">

        <!-- Footer Links -->
            <div class="container text-center text-md-left">

    		<!-- Footer Links -->
    			<div class="row text-center text-md-left mt-3 pb-3">

    				<!-- Grid column -->
    				<div class="col-md-3 col-lg-3 col-xl-3 mx-auto mt-3">
            				
            			<h6 class="text-uppercase text-white font-weight-bold">IEEE IST</h6>	
            			<p>
                            Advancing Technology for Humanity
                        </p>
          				
          			</div>
    				<!-- Grid column -->

    				<hr class="w-100 clearfix d-md-none">

    				<!-- Grid column -->
    				<div class="col-md-2 col-lg-2 col-xl-2 mx-auto mt-3">
            				
            			<h6 class="text-uppercase text-white font-weight-bold">Comunidades</h6>	
            			<p> <a href="#!">CS</a> </p>		
            			<p> <a href="#!">IAS</a> </p>
            			<p> <a href="#!">EMBS</a> </p>	
            			<p> <a href="#!">Wie</a> </p>			
          			</div>
    				<!-- Grid column -->

    				<hr class="w-100 clearfix d-md-none">

    				<!-- Grid column -->
    				<div class="col-md-3 col-lg-2 col-xl-2 mx-auto mt-3">
            				
            			<h6 class="text-uppercase text-white font-weight-bold">Links uteis</h6>	
            			<p> <a href="#!">Eventos</a> </p>
            			<p> <a href="#!">TISP 2.0</a> </p>
            			<p> <a href="#!">Respositorio</a> </p>
          				<p> <a href="#!">Galeria</a> </p>
                        <p> <a href="#!">Membros</a> </p>

          			</div>
    				<!-- Grid column -->

    				<hr class="w-100 clearfix d-md-none">

    				<!-- Grid column -->
    				<div class="col-md-4 col-lg-3 col-xl-3 mx-auto mt-3">
            	
            			<h6 class="text-uppercase text-white font-weight-bold">Contactos</h6>
            			<p> <i class="fas fa-home mr-3"></i> Alameda Av. Rovisco Pais, 11049-001 Lisboa Portugal</p>
                        <p> <i class="fas fa-home mr-3"></i> Taguspark Av. Prof. Doutor Cavaco Silva, 2744-016 Porto Salvo Portugal</p>
     					<p> <i class="fas fa-envelope mr-3"></i> contact@ieee-ist.org</p>
       					<p> <i class="fas fa-phone mr-3"></i> + 351 21 423 3551</p>
          				
          			</div>
    				<!-- Grid column -->				

    			</div>	
    		<!-- Footer Links -->

    		<hr>

    		<!-- Grid row -->
        	<div class="row d-flex align-items-center">

          		<!-- Grid column -->
          		<div class="col-md-7 col-lg-8">

            		<!--Copyright-->
            		<p class="text-center text-md-left">© 2020 Copyright:
              			<a href="https://mdbootstrap.com/education/bootstrap/">
                			<strong> ieee-ist.org</strong>
              			</a>
           			</p>
           			<!--Copyright-->

          		</div>
          		<!-- Grid column -->

         	 	<!-- Grid column -->
          		<div class="col-md-5 col-lg-4 ml-lg-0">

            		<!-- Social buttons -->
            		<div class="text-center text-md-right">
              			
              			<ul class="list-unstyled list-inline">
                			<li class="list-inline-item">
                  				<a class="btn-floating btn-sm rgba-white-slight mx-1"><i class="fab fa-facebook-f"></i></a>
                			</li>
                
                			<li class="list-inline-item">
                  				<a class="btn-floating btn-sm rgba-white-slight mx-1"><i class="fab fa-twitter"></i></a>
                			</li>
                
                			<li class="list-inline-item">
                  				<a class="btn-floating btn-sm rgba-white-slight mx-1"><i class="fab fa-instagram"></i></a>
                			</li>
               
               				<li class="list-inline-item">
                  				<a class="btn-floating btn-sm rgba-white-slight mx-1"><i class="fab fa-linkedin-in"></i></a>
                			</li>
                            <li class="list-inline-item">
                                <a class="btn-floating btn-sm rgba-white-slight mx-1"><i class="fas fa-envelope"></i></i></a>
                            </li>
              			</ul>

            		</div>
            		<!-- Social buttons -->

          		</div>
          		<!-- Grid column -->

        	</div>
       		<!-- Grid row -->

        </div>
        <!-- Footer Links -->

	</footer>
	<!-- Footer -->

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
    
    footer {
        background: steelblue;
        position: relative;
        width: 100%;
    }

    footer p {
        font-size: 0.9em;
        color: white;
    }

    footer p a {
        color: white;
    }

</style>
