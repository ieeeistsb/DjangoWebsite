from django.db import models

from .Volunteer import VolunteerModel

from .Team import TeamModel

class TeamMemberModel(models.Model):

	role   = models.CharField(max_length = 50)
	
	member = models.ForeignKey(VolunteerModel, on_delete = models.CASCADE)

	team   = models.ForeignKey(TeamModel, on_delete = models.CASCADE)

	def __unicode__(self):

		return f'{self.team.__unicode__()} - {self.member.name} with role {self.role}'
