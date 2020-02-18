from django.db import models

from .TranslatableContent import TranslatableContentModel

from .Department import DepartmentModel

from .Event import EventModel

from .Page import PageModel

from .Image import ImageModel

class BranchModel(models.Model):

	name        = models.CharField(max_length = 100, unique = True)

	tag         = models.CharField(max_length = 8, unique = True)

	description = models.ManyToManyField(TranslatableContentModel, blank = True)

	departments = models.ManyToManyField(DepartmentModel, blank = True)

	events      = models.ManyToManyField(EventModel, blank = True)

	pages       = models.ManyToManyField(PageModel, blank = True)

	images      = models.ManyToManyField(ImageModel, blank = True)

	def __str__(self):

		return self.name
