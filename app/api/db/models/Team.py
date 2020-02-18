from django.db import models

from .Member import MemberModel

class TeamModel(models.Model):

	scholar_year = models.CharField(max_length = 5, unique = False)

	members      = models.ManyToManyField(MemberModel)

	def __str__(self):

		return self.scholar_year
