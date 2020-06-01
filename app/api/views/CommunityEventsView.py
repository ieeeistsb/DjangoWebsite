from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from ..io import GetCommunityEventsIO

from ...entities import Community
from ...usecases import get_community_events

if settings.MOCK_DB:
	from ..db import DBHandler
else:
	from ..mocks import MockDBHandler as DBHandler

class CommunityEventsView(APIView):

	def get(self, request):
		io_handler = GetCommunityEventsIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:

			community_events = get_community_events(io_handler, db_handler)

		except Exception as e:
			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(community_events)

