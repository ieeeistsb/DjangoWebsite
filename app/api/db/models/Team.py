from django.db import models

from typing import List

from .Member import MemberModel

class TeamModel(models.Model):

	scholar_year = models.CharField(max_length = 5, unique = False)

	members_ids  = models.ManyToManyField(MemberModel, through='TeamMemberModel', related_name='team_members')

	def members(self) -> List[MemberModel]:

		return self.members_ids.all()

	def __str__(self):

		return self.scholar_year

class TeamMemberModel(models.Model):

	ROLES = [("chair", "chair"), ("vice-chair", "vice-chair"), ("collaborator", "collaborator"), ("treasurer", "treasurer"), ("secretary", "secretary"), ("coordinator", "coordinator"), ("innovation-manager", "innovation-manager")]

	team_id   = models.ForeignKey(TeamModel, on_delete=models.CASCADE)

	member_id = models.ForeignKey(MemberModel, on_delete=models.CASCADE)

	role      = models.CharField(max_length = 20, choices=ROLES)

	def __str__(self):

		return str(self.team_id)
