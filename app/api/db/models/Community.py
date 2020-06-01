from django.db import models

from typing import List

from .Image import ImageModel

from .Page import PageModel

from .Event import EventModel

from .Department import DepartmentModel

from .TranslatableContent import TranslatableContentModel

from ....entities import Community

class CommunityModel(models.Model):

	tag             = models.CharField(max_length = 8, unique = True, primary_key=True)

	name            = models.CharField(max_length = 100, unique = True)

	description_ids = models.ManyToManyField(TranslatableContentModel, blank = True)

	images_ids      = models.ManyToManyField(ImageModel, blank = True)

	pages_types_ids = models.ManyToManyField(PageModel, blank = True)

	events_ids      = models.ManyToManyField(EventModel, blank = True)

	departments_ids = models.ManyToManyField(DepartmentModel, blank = True)

	def description(self, lang : str) -> List[str]:

		description = [content_model.content(lang) for content_model in self.description_ids.all()]

		return description

	def images(self) -> List[ImageModel]:

		return self.images_ids.all()

	def events(self) -> List[EventModel]:

		return self.events_ids.all()

	def departments(self) ->List[DepartmentModel]:

		return self.departments_ids.all()

	def pages(self) -> List[PageModel]:

		return self.pages_types_ids.all()

	def toEntity(self, lang : str) -> Community:

		images = [image.url() for image in self.images()]

		pages = [page.toEntity(lang) for page in self.pages()]

		return Community(self.name, self.tag, self.description(lang), images, pages)

	def __str__(self):

		return self.name
