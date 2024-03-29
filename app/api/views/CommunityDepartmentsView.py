from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from ..io import GetCommunityDepartmentsIO

from ...usecases import get_community_departments

if settings.MOCK_DB:
	from ..mocks import MockDBHandler as DBHandler
else:
	from ..db import DBHandler

class CommunityDepartmentsView(APIView):

	def get(self, request):

		io_handler = GetCommunityDepartmentsIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:

			community_departments = get_community_departments(io_handler, db_handler)

		except Exception as e:

			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(community_departments)
