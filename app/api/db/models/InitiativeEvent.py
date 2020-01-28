from django.db import models

from .TranslatableTitle import TranslatableTitleModel

from .TranslatableContent import TranslatableContentModel

from .Initiative import InitiativeModel

from .Path import Path

class InitiativeEventModel(TranslatableTitleModel, TranslatableContentModel):

	image      = models.ImageField(upload_to = Path.getInitiativesPath())

	date       = models.DateTimeField()

	initiative = models.ForeignKey(InitiativeModel, on_delete = models.CASCADE) 

	facebook   = models.URLField(blank = True, null = True)

	def __unicode__(self):

		return self.initiative.__unicode__()


