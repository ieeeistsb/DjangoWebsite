from django.db import models

from typing import List

from .Team import TeamModel

from .Team import TeamMemberModel

from .TranslatableContent import TranslatableContentModel

from ....entities import Department

class DepartmentModel(models.Model):

	name_id    = models.ForeignKey(TranslatableContentModel, on_delete=models.CASCADE)

	teams_ids  = models.ManyToManyField(TeamModel, blank = True, related_name='department_teams')

	def name(self, lang : str) -> str:

		content_model = self.name_id

		return content_model.content(lang)

	def teams(self) -> List[TeamModel]:

		return self.teams_ids.all()

	def team(self, scholar_year : str) -> TeamModel:

		for team_model in self.teams():

			if team_model.scholar_year == scholar_year:

				return team_model

	def toEntity(self, lang : str, scholar_year : str) -> Department:

		team = self.team(scholar_year)

		members = []

		if not team is None:

			for member in team.members():

				role = TeamMemberModel.objects.filter(member_id=member)[0].role

				member_entity = member.toEntity(lang, role)

				members += [member_entity]

		return Department(self.name(lang), members)

	def __str__(self):

		return self.name('pt')
