from django.db import models

from .TranslatableContent import TranslatableContentModel

from .Image import ImageModel

class BookModel(models.Model):

	title        = models.CharField(max_length = 100)

	author       = models.CharField(max_length = 100)

	year_edition = models.CharField(max_length = 30)

	price        = models.CharField(max_length = 15)

	quality_id   = models.ForeignKey(TranslatableContentModel, on_delete=models.CASCADE)

	contact      = models.CharField(max_length = 80)

	image_id     = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	def quality(self, lang : str) -> str:

		content_model = self.quality_id

		return content_model.content(lang)

	def image(self) -> ImageModel:

		return self.image_id

	def __str__(self):

		return self.title
