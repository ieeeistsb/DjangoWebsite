from django.db import models

from .Volunteer import VolunteerModel;

from .Path import Path

class CommunityModel(models.Model):

	name       = models.CharField(max_length = 100, unique = True)

	chair      = models.ManyToManyField(VolunteerModel, blank = True, related_name = 'chair')

	vice_chair = models.ManyToManyField(VolunteerModel, related_name = 'vice_chair')

	info_en    = models.TextField()

	info_pt    = models.TextField()

	image      = models.ImageField(upload_to = Path.getCommunitiesPath(), blank = True)

	newsletter_subscribe_url = models.URLField(blank = True, null = True)

	def __unicode__(self):

		return self.name
