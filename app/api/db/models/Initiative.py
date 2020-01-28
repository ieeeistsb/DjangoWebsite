from django.db import models

from .TranslatableTitle import TranslatableTitleModel

from .TranslatableContent import TranslatableContentModel

from .Partner import PartnerModel

from .Path import Path

class InitiativeModel(TranslatableTitleModel, TranslatableContentModel):

	community = models.URLField(blank = True, null = True)

	partners  = models.ManyToManyField(PartnerModel, blank = True)

	image     = models.ImageField(upload_to = Path.getInitiativesPath(), blank = True, null = True)
