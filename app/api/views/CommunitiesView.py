from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from ..io import GetCommunitiesIO

from ...usecases import get_communities

#from ..db import DBHandler
from ..mocks import MockDBHandler as DBHandler

class CommunitiesView(APIView):

	def get(self, request):
		io_handler = GetCommunitiesIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:
			#call usecase
			communities = get_communities(io_handler, db_handler)

		except Exception as e:
			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(communities)

