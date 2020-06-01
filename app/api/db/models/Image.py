from django.db import models

class ImageModel(models.Model):

	PATH_BASE = 'images/'

	image = models.ImageField(upload_to = PATH_BASE)

	def url(self):

		return self.image.url

	def __str__(self):

		return self.image.url
