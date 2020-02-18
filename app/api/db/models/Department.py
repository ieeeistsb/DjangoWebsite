from django.db import models

from .Team import TeamModel

class DepartmentModel(models.Model):

	name       = models.CharField(max_length = 100, unique = False)

	teams      = models.ManyToManyField(TeamModel, blank = True)

	def __str__(self):

		return self.name
