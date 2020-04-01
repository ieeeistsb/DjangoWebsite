from django.db import models

class TranslatableContentModel(models.Model):

	content_en = models.TextField()

	content_pt = models.TextField()

	def content(self, lang : str) -> str:

		field = 'content_' + lang

		return getattr(self, field)

	def __str__(self):

		return self.content_en