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

            <form class="col-md-4">
                <div class="form-group row">
                    <label for="scholarYear" class="col-sm-3 col-form-label">{{lang==='pt' ? 'Ano Escolar:' : 'Scholar Year:'}}</label>
                    <select id="scholarYear" v-model="scholarYear" class="form-control col-sm-2">
                        <option>16/17</option>
                        <option>17/18</option>
                        <option>18/19</option>
                        <option selected>19/20</option>
                        <option>20/21</option>
                    </select>
                </div>
            </form>

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

        public scholarYear: string = "19/20";

		/*public departments : Department[] = [
            {'name': 'Board', 'members' : 
                [
                {'name':'Joana Nápoles', 'role':'Chair', 'description': 'A Joana entrou para o IEEE-IST SB como colaboradora do projeto Younique no início do ano de 2018. No ano de 2018/2019 entrou para a EMBS-IST como Innovation Manager, cargo que ocupa atualmente, como membro ativo na direção. \n\n\nNeste cargo tem a oportunidade de garantir que cada iniciativa e departamento cresça da melhor forma, contribuindo para a motivação de cada equipa e o sucesso dos alunos da nossa instituição. As principais características que a movem são a sua paixão por ajudar o próximo e a sua ambição para fazer o seu melhor em tudo.', 'image': 'JoanaNapoles2.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'},
                {'name':'Filipa Rocha', 'role':'Vice-Chair', 'description': 'Hi, I am asdasdaed', 'image':'FilipaRocha.jpg'}
                ]
            }
        ];*/

        async created() {
            try {
                this.departments = (await CommunityApi.get_community_departments(this.tag, this.lang, this.scholarYear)).reverse();
                this.orderDepartments();
            } catch(error) {
                alert(error);
            }
        }

        @Watch('tag')
        public async onTagUpdate(value, oldValue) {
            try {
                this.departments = (await CommunityApi.get_community_departments(this.tag, this.lang, this.scholarYear)).reverse();
                this.orderDepartments();
            } catch(error) {
                alert(error);
            }
        }

        @Watch('scholarYear')
        public async onScholarYearUpdate(value, oldValue) {
            try {
                this.departments = (await CommunityApi.get_community_departments(this.tag, this.lang, this.scholarYear)).reverse();
                this.orderDepartments();
            } catch(error) {
                alert(error);
            }
        }

        public orderDepartments() {

            this.departments.sort(function (dep1, dep2) {
                if (dep1.name > dep2.name) return  1;
                if (dep1.name < dep2.name) return -1;
                return 0;
            });

            this.departments.forEach((dep) => {
                dep.members.sort(function (m1, m2) {

                    if (m1.role == m2.role) {
                        if (m1.name > m2.name) return  1;
                        if (m1.name < m2.name) return -1;
                        return 0;
                    }

                    if (m1.role == "chair") return -1;
                    if (m2.role == "chair") return  1;

                    if (m1.role == "vice-chair") return -1;
                    if (m2.role == "vice-chair") return  1;

                    if (m1.role == "treasurer") return -1;
                    if (m2.role == "treasurer") return  1;

                    if (m1.role == "secretary") return -1;
                    if (m2.role == "secretary") return  1;

                    if (m1.role == "innovation-manager") return -1;
                    if (m2.role == "innovation-manager") return  1;

                    if (m1.role == "coordinator") return -1;
                    if (m2.role == "coordinator") return  1;

                    if (m1.role == "collaborator") return -1;
                    if (m2.role == "collaborator") return  1;
                });
            });
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