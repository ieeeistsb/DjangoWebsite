<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Newsletter</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span v-if="lang==='pt'">A Newsletter é uma edição mensal que procura escrutinar as actividades da própria organização e da comunidade do Técnico de uma forma informativa e crítica, bem como dar voz à força motora que permitirá assegurar a continuidade desta comunidade – professores e alunos.
			</span>
			<span v-else>The Newsletter is a monthly edition that seeks to scrutinize the activities of the organization itself and the Técnico community in an informative and critical way, as well as giving a voice to the driving force that will ensure the continuity of this community - teachers and students.
			</span>
		</p>

		<p>&nbsp;</p>

		<h1 class='m-about-title'>
			<strong><span>{{lang==='pt' ? 'Os Nossos Artigos' : 'Our Articles'}}</span></strong>
		</h1>

		<p>&nbsp;</p>

		<div id="newsletter_content" class="container mt-5">
            
            <div id="news_year" class="row mt-5" v-for='year in years'>
        		<div id="news_year_title" class="col-12 mb-4">
                    <h5 class="h4">{{year}}</h5>
                </div>

                <div id="news" class="col-xs-12 col-sm-6 col-md-4" v-for='news in newsList'>
                	<div  @click="changeSelectedNews(news)" data-toggle="modal" data-target=".bd-example-modal-lg">
                		<news-card :news='news'/>
                	</div>
        			
        		</div>
            
            </div>
	    
        </div>

		<p>&nbsp;</p>

		<!--News Modal-->
		<div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
			<div class="modal-dialog modal-lg">

				<!--Modal Content-->
				<div class="modal-content">

					<!--Modal Header-->
					<div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel">{{selectedNews ? selectedNews.title : ''}}</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close" >
							<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<!--/.Modal Header-->

					<!--Modal Body-->
					<div class="modal-body" v-if="selectedNews">
						
						<p class='card-text'>
							<span v-for='paragraph in selectedNews.text'>
								{{paragraph}}
								<br><br>
							</span>
						</p>

					</div>
					<!--/.Modal Body-->

					<!--Modal Footer-->
					<div class="modal-footer">

						<h5>{{selectedNews ? selectedNews.author : ''}}</h5>

					</div>
					<!--/.Modal Footer-->

				</div>
				<!--/.Modal Content-->
			</div>
		</div>
		<!--/.News Modal-->

	</div>
</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import NewsCard from '../components/NewsCard.vue';

	import { News } from '../api/entities.ts';

	import CommunityApi from '../api/CommunityApi.ts';

	@Component({ components: { 'news-card': NewsCard, }, })
	export default class NewsletterView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public lang: string = this.$store.getters.getLang;

		public selectedNews: News | null = null;

		public newsList: News[] = [
			{
				'year': 2019,
				'author':'Carolina Caramelo',
				'title':'O Cérebro Dependente',
				'text': ['Mil milhões de pessoas em todo o mundo são fumadoras, quase um em cada vinte adultos é dependente de álcool, mais de três milhões de mortes por ano no mundo estão associadas a este, noventa e um americanos morrem todos os dias devido a overdoses de drogas. O que move cegamente estas pessoas que entram num loop vicioso, que pode nunca ter um fim? O desejo insaciável, as obsessões e compulsões incontroláveis. A emoção súbita, a constante e cíclica procura de elevar a fasquia de modo a continuar a sentir o êxtase e o coração a palpitar.',
				'Como funciona este processo de autodestruição, alimentado por hábitos compulsivos, continua a ser motivo de estudo entre a comunidade científica que procura uma saída deste ciclo que prende dezenas de milhões de pessoas à volta do globo.',
				'A dependência apropria-se das vias neuronais do cérebro remodelando os circuitos neuronais de modo a atribuir um valor supremo seja ao álcool, drogas, tabaco ou até mesmo ao jogo, em detrimento de outros interesses como a família, o trabalho, a saúde ou a própria vida.',
				'Até há pouco tempo a ideia de reparar as ligações cerebrais para combater a dependência pareceria improvável. Contudo, o avanço tecnológico e os progressos da neurociência vieram modificar radicalmente as noções convencionais sobre a dependência.',
				'O que os cientistas referem há anos é que dependência é uma doença e não um fracasso moral, não sendo necessariamente caracterizada por uma dependência física ou abstinência, mas sim pela repetição compulsiva de uma atividade, apesar das consequências nocivas que esta última possa ter para a vida. Tal ponto de vista, levou muitos cientistas a aceitar a ideia de que é possível existir dependência sem drogas. Alguns creem mesmo que muitos atrativos da vida contemporânea, como o fast food, as compras e os smartphones são potencialmente viciantes devido aos efeitos poderosos que exercem no sistema de recompensa do cérebro – o circuito subjacente à compulsão, uma parte primitiva do cérebro que existe para garantir que procuramos aquilo que queremos e alerta nos para sons, odores e imagens que nos possam encaminhar até lá.',
				'Anna Rose Childress, diretora do Brain-Behavioral Vulnerabilities Laboratory of the Center for Studies of Addiction, e outros cientistas têm tentado desvendar os mistérios da dependência estudando o sistema de recompensa. Grande parte da investigação implica a introdução de pessoas dependentes de drogas no tubo de um equipamento de ressonância magnética que detecta o fluxo sanguíneo no cérebro como uma forma de analisar a atividade neuronal. Através de algoritmos complexos de aplicação de códigos cromáticos, os exames cerebrais são convertidos em imagens identificadoras dos circuitos que são ativados quando o cérebro deseja algo.',
				'O nosso sistema de recompensa opera no reino do instinto e dos reflexos, prejudicando-nos num mundo que nos dá a oportunidade de satisfazermos desejos vinte e quatro horas por dia.'
				]
			}
		];

		public years: number[] = [];

		async created() {
			try {
				// this.newsList = (await CommunityApi.get_community_news(this.tag, this.lang)).reverse();
				this.orderNews();
			} catch(error) {
				alert(error);
			}
		}

		@Watch('tag')
		public async onTagUpdate(value, oldValue) {
			try {
				// this.newsList = (await CommunityApi.get_community_news(this.tag, this.lang)).reverse();
				this.orderNews();
			} catch(error) {
				alert(error);
			}
		}

		public orderNews() {

			this.newsList.sort((n1, n2) => {
				if (n1.year > n2.year) return  1;
                if (n1.year < n2.year) return -1;
                return 0;
			});

			this.newsList.forEach((news) => {
				if (this.years.indexOf(news.year) < 0)
					this.years.push(news.year);
			});
		}

		public changeSelectedNews(news: News) {
			this.selectedNews = news;
		}

	}

</script>

<style scoped>
	
	.m-about-title {
		text-align: center;
		color: #808080;
	}

	.m-about-text {
		text-align: justify;
		color: #808080;
		margin-left: 10%;
		margin-right: 10%;
	}

	.card-text {
		height: 450px;
		overflow-y: scroll;
		overflow-x: hidden;
		text-align: justify;
	}

	#news_year_title {
        text-align: center;
        color: #007b5e;
        text-transform: uppercase;
    }

</style>