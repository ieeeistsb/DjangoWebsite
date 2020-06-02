from django.db import models

from typing import List

from .TranslatableContent import TranslatableContentModel

from .Department import DepartmentModel

from .Event import EventModel

from .Page import PageModel

from .Image import ImageModel

from ....entities import Branch

class BranchModel(models.Model):

	name            = models.CharField(max_length = 100, unique = True, primary_key=True)

	description_ids = models.ManyToManyField(TranslatableContentModel, blank = True, related_name='branch_description')

	departments_ids = models.ManyToManyField(DepartmentModel, blank = True, related_name='branch_departments')

	events_ids      = models.ManyToManyField(EventModel, blank = True, related_name='branch_events')

	pages_types_ids = models.ManyToManyField(PageModel, blank = True, related_name='branch_pages')

	images_ids      = models.ManyToManyField(ImageModel, blank = True, related_name='branch_images')

	def description(self, lang : str) -> List[str]:

		description = [content_model.content(lang) for content_model in self.description_ids.all()]

		return description

	def departments(self) -> List[DepartmentModel]:

		return self.departments_ids.all()

	def events(self) -> List[EventModel]:

		return self.events_ids.all()

	def images(self) -> List[str]:

		return self.images_ids.all()

	def pages(self) -> List[PageModel]:

		return self.pages_types_ids.all()

	def toEntity(self, lang : str) -> Branch:

		images = [image.url() for image in self.images()]

		pages = [page.toEntity(lang) for page in self.pages()]

		return Branch(self.name, self.description(lang), images, pages)

	def __str__(self):

		return self.name
