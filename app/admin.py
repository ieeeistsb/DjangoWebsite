from django.contrib import admin

# Register your models here.

from .api.db.models import *

admin.site.register(CommunityModel)

admin.site.register(InitiativeModel)

admin.site.register(InitiativeEventModel)

admin.site.register(NewsModel)

admin.site.register(NewsletterModel)

admin.site.register(PartnerModel)

admin.site.register(SocialNetworkModel)

admin.site.register(TagModel)

admin.site.register(TeamModel)

admin.site.register(TeamMemberModel)

admin.site.register(VolunteerModel)
