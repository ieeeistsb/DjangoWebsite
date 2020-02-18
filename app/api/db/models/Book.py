from django.db import models

from .Image import ImageModel

class BookModel(models.Model):

	title        = models.CharField(max_length = 100, unique = True)

	author       = models.CharField(max_length = 100)

	year_edition = models.CharField(max_length = 30)

	price        = models.CharField(max_length = 15)

	quality      = models.CharField(max_length = 80)

	contact      = models.CharField(max_length = 80)

	image        = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	def __str__(self):

		return self.title
