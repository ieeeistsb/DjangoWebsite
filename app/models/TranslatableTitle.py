from django.db import models

class TranslatableTitleModel(models.Model):

	title_en = models.CharField(max_length = 100)

	title_pt = models.CharField(max_length = 100)

	class Meta:

		abstract = True

	def __unicode__(self):

		return self.title_en

