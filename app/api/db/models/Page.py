from django.db import models

from .Image import ImageModel

from .TranslatableContent import TranslatableContentModel

from ....entities import Page

class PageModel(models.Model):

	TYPES   = [("members", "members"), ("events", "events"), ("repository", "repository")]

	type    = models.CharField(max_length = 20, choices=TYPES, unique = True, primary_key=True)

	name_id = models.OneToOneField(TranslatableContentModel, related_name='page_name', on_delete=models.CASCADE)

	def name(self, lang : str) -> str:

		content_model = self.name_id

		return content_model.content(lang)

	def toEntity(self, lang : str) -> Page:

		return Page(self.type, self.name(lang))

	def __str__(self):

		return self.name('en')
