'''
API Endpoints
'''

from django.urls import path

from .views import BranchView, BranchDepartmentsView, BranchEventsView

from .views import CommunitiesView, CommunityEventsView, CommunityDepartmentsView

urlpatterns = [
	path('v1/branch/', BranchView.as_view()),
	path('v1/branch/departments/', BranchDepartmentsView.as_view()),
	path('v1/branch/events/', BranchEventsView.as_view()),
	path('v1/communities/', CommunitiesView.as_view()),
	path('v1/community/events/', CommunityEventsView.as_view()),
	path('v1/community/departments/', CommunityDepartmentsView.as_view())
]
