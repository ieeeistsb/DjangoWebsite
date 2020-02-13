'''
API Endpoints
'''

from django.urls import path

from .views import CommunitiesView, CommunityEventsView

urlpatterns = [
	path('v1/communities/', CommunitiesView.as_view()),
	path('v1/community/events/', CommunityEventsView.as_view()),
]
