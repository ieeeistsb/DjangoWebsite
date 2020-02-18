from django.db import models

class TranslatableContentModel(models.Model):

	content_en = models.TextField()

	content_pt = models.TextField()
