from django.db import models

class TeamModel(models.Model):

	begin_year = models.IntegerField()

	end_year   = models.IntegerField()

	def __unicode__(self):

		return str(self.begin_year) + '/' + str(self.end_year)
