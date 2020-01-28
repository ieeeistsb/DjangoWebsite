from django.db import models

from .SocialNetwork import SocialNetworkModel

from .Path import Path

class VolunteerModel(models.Model):

	name    = models.CharField(max_length = 100)

	email   = models.EmailField(unique = True, null = True)

	socials = models.ManyToManyField(SocialNetworkModel, blank = True)

	image   = models.ImageField(upload_to = Path.getVolunteersPath())

	def __unicode__(self):
		return self.name
