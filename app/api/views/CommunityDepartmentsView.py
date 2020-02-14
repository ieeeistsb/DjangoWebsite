from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from ..io import GetCommunityDepartmentsIO

from ...entities import Community
from ...usecases import get_community_departments

#from ..db import DBHandler
from ..mocks import MockDBHandler as DBHandler

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

