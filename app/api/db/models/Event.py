from django.db import models

from typing import List

from .Image import ImageModel

from .TranslatableContent import TranslatableContentModel

from ....entities import Event

class EventModel(models.Model):

	name            = models.CharField(max_length = 50)

	date_time       = models.DateTimeField()

	image_id        = models.ForeignKey(ImageModel, on_delete=models.CASCADE)

	description_ids = models.ManyToManyField(TranslatableContentModel, blank = True, related_name='event_description')

	def image(self) -> List[ImageModel]:

		return self.image_id

	def description(self, lang : str) -> List[str]:

		description = [content_model.content(lang) for content_model in self.description_ids.all()]

		return description

	def toEntity(self, lang : str) -> Event:

		return Event(self.name, str(self.date_time), self.description(lang), self.image().url())

	def __str__(self):

		return self.name
