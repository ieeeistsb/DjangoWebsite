from django.contrib import admin

# Register your models here.

from .api.db.models import *

admin.site.register(BookModel)

admin.site.register(BranchModel)

admin.site.register(CommunityModel)

admin.site.register(DepartmentModel)

admin.site.register(EventModel)

admin.site.register(ImageModel)

admin.site.register(MemberModel)

admin.site.register(PageModel)

admin.site.register(TeamModel)

admin.site.register(TeamMemberModel)

admin.site.register(TranslatableContentModel)
