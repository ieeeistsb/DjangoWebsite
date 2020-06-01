from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from ..io import GetBranchEventsIO

from ...usecases import get_branch_events

if settings.MOCK_DB:
	from ..db import DBHandler
else:
	from ..mocks import MockDBHandler as DBHandler

class BranchEventsView(APIView):

	def get(self, request):

		io_handler = GetBranchEventsIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:

			branch_events = get_branch_events(io_handler, db_handler)

		except Exception as e:

			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(branch_events)
