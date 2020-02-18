from django.db import models

from .Image import ImageModel

from .Page import PageModel

from .Event import EventModel

from .Department import DepartmentModel

class CommunityModel(models.Model):

	name        = models.CharField(max_length = 100, unique = True)

	tag         = models.CharField(max_length = 8, unique = True)

	images      = models.ManyToManyField(ImageModel, blank = True)

	pages       = models.ManyToManyField(PageModel, blank = True)

	events      = models.ManyToManyField(EventModel, blank = True)

	departments = models.ManyToManyField(DepartmentModel, blank = True)

	def __str__(self):

		return self.name
