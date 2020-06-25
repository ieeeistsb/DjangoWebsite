<template>

	<section id="team" class="pb-5">

        <div id=team_header class="container">

            <div class="row mt-5">
                <div class="col-12">
                    <h1 class='m-about-title'>
                        <strong><span>{{lang==='pt' ? 'Membros' : 'Members'}}</span></strong>
                    </h1>
                </div>
            </div>

        </div>

		<div id="team_content" class="container mt-5">
            
            <div id="department" class="row mt-5" v-for='dep in departments'>
        		<div id="department_title" class="col-12 mb-4">
                    <h5 class="h4">{{dep.name}}</h5>
                </div>

                <div id="department_member" class="col-xs-12 col-sm-6 col-md-4" v-for='member in dep.members'>
        			<member-card :member='member' />
        		</div>
            
            </div>
	    
        </div>
    
    </section>

</template>

<script lang='ts'>

	import { Vue, Component, Prop, Watch } from 'vue-property-decorator';

	import MemberCard from '../components/MemberCard.vue';

	import CommunityApi from '../api/CommunityApi.ts';

	import { Member, Department } from '../api/entities.ts';

	@Component({ components: { 'member-card': MemberCard, }, })
	export default class TeamView extends Vue {

		@Prop({ required: true, })
		public tag: string;

		public lang: string = this.$store.getters.getLang;

        public departments: Department[] = [];

		/*public departments : Department[] = [
            {'name': 'Board', 'members' : 
                [
                {'name':'Joana Nápoles', 'role':'Chair', 'description': 'A Joana entrou para o IEEE-IST SB como colaboradora do projeto Younique no início do ano de 2018. No ano de 2018/2019 entrou para a EMBS-IST como Innovation Manager, cargo que ocupa atualmente, como membro ativo na direção. \n\n\nNeste cargo tem a oportunidade de garantir que cada iniciativa e departamento cresça da melhor forma, contribuindo para a motivação de cada equipa e o sucesso dos alunos da nossa instituição. As principais características que a movem são a sua paixão por ajudar o próximo e a sua ambição para fazer o seu melhor em tudo.', 'image': 'JoanaNapoles2.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'}
                ]
            },
            {'name': 'Board', 'members' : 
                [
                {'name':'Joana Nápoles', 'role':'Chair', 'description': 'A Joana entrou para o IEEE-IST SB como colaboradora do projeto Younique no início do ano de 2018. No ano de 2018/2019 entrou para a EMBS-IST como Innovation Manager, cargo que ocupa atualmente, como membro ativo na direção. Neste cargo tem a oportunidade de garantir que cada iniciativa e departamento cresça da melhor forma, contribuindo para a motivação de cada equipa e o sucesso dos alunos da nossa instituição. As principais características que a movem são a sua paixão por ajudar o próximo e a sua ambição para fazer o seu melhor em tudo.', 'image': 'JoanaNapoles2.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'}
                ]
            },
            {'name': 'Board', 'members' : 
                [
                {'name':'Joana Nápoles', 'role':'Chair', 'description': 'A Joana entrou para o IEEE-IST SB como colaboradora do projeto Younique no início do ano de 2018. No ano de 2018/2019 entrou para a EMBS-IST como Innovation Manager, cargo que ocupa atualmente, como membro ativo na direção. Neste cargo tem a oportunidade de garantir que cada iniciativa e departamento cresça da melhor forma, contribuindo para a motivação de cada equipa e o sucesso dos alunos da nossa instituição. As principais características que a movem são a sua paixão por ajudar o próximo e a sua ambição para fazer o seu melhor em tudo.', 'image': 'JoanaNapoles2.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'}
                ]
            },
            {'name': 'Board', 'members' : 
                [
                {'name':'Joana Nápoles', 'role':'Chair', 'description': 'A Joana entrou para o IEEE-IST SB como colaboradora do projeto Younique no início do ano de 2018. No ano de 2018/2019 entrou para a EMBS-IST como Innovation Manager, cargo que ocupa atualmente, como membro ativo na direção. Neste cargo tem a oportunidade de garantir que cada iniciativa e departamento cresça da melhor forma, contribuindo para a motivação de cada equipa e o sucesso dos alunos da nossa instituição. As principais características que a movem são a sua paixão por ajudar o próximo e a sua ambição para fazer o seu melhor em tudo.', 'image': 'JoanaNapoles2.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'}
                ]
            }
        ];*/

        async created() {
            try {
                this.departments = (await CommunityApi.get_community_departments(this.tag, this.lang)).reverse();
            } catch(error) {
                alert(error);
            }
        }

        @Watch('tag')
        public async onTagUpdate(value, oldValue) {
            try {
                this.departments = (await CommunityApi.get_community_departments(this.tag, this.lang)).reverse();
            } catch(error) {
                alert(error);
            }
        }

        public returnClass(idx) : string {
            if (idx == 0)
                return "m-item carousel-item active";
            
            return "m-item carousel-item";
        }
 	}

</script>

<style scoped>
        
    #department_title {
        text-align: center;
        color: #007b5e;
        text-transform: uppercase;
    }

    .m-about-title {
        text-align: center;
        color: #808080;
    }

    .m-about-text {
        text-align: center;
        color: #808080;
    }

</style>