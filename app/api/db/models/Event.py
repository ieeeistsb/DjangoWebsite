from django.db import models

from .Image import ImageModel

from .TranslatableContent import TranslatableContentModel

class EventModel(models.Model):

	name  = models.CharField(max_length = 50)

	date  = models.DateTimeField()

	image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	description = models.ManyToManyField(TranslatableContentModel, blank = True)

	def __str__(self):

		return self.name
