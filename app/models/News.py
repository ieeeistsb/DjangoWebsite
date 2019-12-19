from django.db import models

from .Tag import TagModel

from .Path import Path

class NewsModel(models.Model):

	date  = models.DateTimeField(auto_now_add = False)

	image = models.ImageField(upload_to = Path.getNewsPath(), null = True, blank = True)

	tags  = models.ManyToManyField(TagModel, blank = True)

	def __unicode__(self):

		return self.name 