'''
FE endpoints
Its just one cause its a single page application
'''

from django.urls import path
from .views import AppView

urlpatterns = [
    path('', AppView.as_view()),
]
