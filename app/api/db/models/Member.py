from django.db import models

from typing import List

from .TranslatableContent import TranslatableContentModel

from .Image import ImageModel

from ....entities import Member

class MemberModel(models.Model):

	name            = models.CharField(max_length = 50)

	mail            = models.CharField(max_length = 50, default = "")

	linkedin        = models.CharField(max_length = 70, default = "")

	description_ids = models.ManyToManyField(TranslatableContentModel, blank = True)

	image_id        = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	def description(self, lang : str) -> List[str]:

		description = [content_model.content(lang) for content_model in self.description_ids.all()]

		return description

	def image(self) -> ImageModel:

		return self.image_id

	def toEntity(self, lang : str) -> Member:

		return Member(self.name, self.mail, self.linkedin, self.description(lang), self.image().url())

	def __str__(self):

		return self.name
