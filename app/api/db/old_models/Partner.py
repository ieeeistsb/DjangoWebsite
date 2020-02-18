from django.db import models

from .Path import Path

class PartnerModel(models.Model):

	url   = models.URLField(blank = True, null = True)

	name  = models.CharField(max_length = 128)

	image = models.ImageField(upload_to = Path.getPartnersPath())

	def __unicode__(self):

		return self.name 