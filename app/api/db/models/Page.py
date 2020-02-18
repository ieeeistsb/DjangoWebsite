from django.db import models

from .Image import ImageModel

from .TranslatableContent import TranslatableContentModel

class PageModel(models.Model):

	type    = models.CharField(max_length = 15)

	name    = models.ManyToManyField(TranslatableContentModel)

	def __str__(self):

		return self.name
