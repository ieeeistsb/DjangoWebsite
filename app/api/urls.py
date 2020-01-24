'''
API Endpoints
'''

from django.urls import path

from .views import CommunitiesView

urlpatterns = [
	path('v1/communities/', CommunitiesView.as_view()),
]
