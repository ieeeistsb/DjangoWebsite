<template>
	<div>
		<p>&nbsp;</p>
		<h1 class='m-about-title'>
			<strong><span>Repositório de Livros e Sebentas</span></strong>
		</h1>
		<p>&nbsp;</p>

		<p class='m-about-text'>
			<span>Já está disponível nesta página um repositório que tem o objectivo de dar aos alunos a possibilidade de comprar e vender material de estudo usado como livros, sebentas ou outros documentos académicos.
			</span>
		</p>

		<p class='m-about-text'>
			<span>Este repositório foca-se principalmente nos alunos do Taguspark e, portanto, nas áreas de Matemática, Física e Química, Economia e Gestão, Informática e Electrónica. No entanto é aberto a qualquer aluno do IST que esteja interessado em vender ou comprar.
			</span>
		</p>

		<p class='m-about-text'>
			<span>Caso pretendas que o teu produto seja aqui anunciado clica no botão abaixo para preencher o formulário ou contacta-nos para o e-mail: <a href='mailto:ias@ieee-ist.org'>ias@ieee-ist.org</a>
			</span>
		</p>

		<p class='m-about-text'>
			<span>Se estiveres interessado em comprar algum livro ou sebenta, só tens de contactar o vendedor!
			</span>
		</p>

		<p>&nbsp;</p>

		<p class='m-sell-tag'>
			<!-- Missing Icon-->
			<a href='https://docs.google.com/forms/d/1Y4pfhLkIVNKVGUGL2uaMwgSEEhzkDCvqQNFJd_79LwM/' class='btn btn-primary' target='_blank'>
				Está interessado em vender?
			</a>
		</p>

		<p>&nbsp;</p>

		<div v-for='book in books'>


			
		</div>

	</div>
</template>

<script lang='ts'>

	import { Vue, Component } from 'vue-property-decorator';

	interface Book {
		title: string;
		author: string;
		year_edition: string;
		price: string;
		quality: string;
		contact: string;
	}

	@Component({})
	export default class RepositoryView extends Vue {

		public books: Book[] = [
			{'title': 'Hidráulica',
			 'author': 'António de Carvalho Quintela',
			 'year_edition': '11ª Edição',
			 'price': '7 IAS',
			 'quality': 'Como novo',
			 'contact': 'antoniossbc@gmail.com'
			},
			{'title': 'Análise Complexa e Equações Diferenciais',
			 'author': 'Luís Barreira',
			 'year_edition': '1ª Edição',
			 'price': '10 IAS',
			 'quality': 'Muito pouco sublinhado',
			 'contact': 'antoniossbc@gmail.com'
			},
		];

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
	
	.m-sell-tag {
		text-align: center;
	}

	.m-sell-tag a {
		background-color: steelblue;
		text-decoration-color: white;
	}

</style>