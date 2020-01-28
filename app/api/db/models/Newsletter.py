from django.db import models

from .TranslatableTitle import TranslatableTitleModel

from .Community import CommunityModel

from .Path import Path

#TODO: Implement PdfValidator

class NewsletterModel(TranslatableTitleModel):

	created      = models.DateTimeField(auto_now_add = True)

	publish_date = models.DateTimeField(blank = False, null = False)

	pdf          = models.FileField(upload_to = Path.getNewsletterPath(), blank = False, null = False)

	community    = models.ForeignKey(CommunityModel, on_delete = models.CASCADE, blank = False, null = False)
