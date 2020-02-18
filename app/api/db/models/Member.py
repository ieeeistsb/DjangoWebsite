from django.db import models

from .TranslatableContent import TranslatableContentModel

from .Image import ImageModel

class MemberModel(models.Model):

	name  = models.CharField(max_length = 50)

	contact = models.CharField(max_length = 30)

	description = models.ManyToManyField(TranslatableContentModel, blank = True)

	image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	def __str__(self):

		return self.name
