from django.db import models

class ImageModel(models.Model):

	PATH_BASE = 'app/api/db/imgs/'

	image = models.ImageField(upload_to = PATH_BASE)

	def __str__(self):

		return self.image.url
