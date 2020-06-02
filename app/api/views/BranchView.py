from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from ..io import GetBranchIO

from ...usecases import get_branch

if settings.MOCK_DB:
	from ..mocks import MockDBHandler as DBHandler
else:
	from ..db import DBHandler

class BranchView(APIView):

	def get(self, request):
		io_handler = GetBranchIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:
			#call usecase
			branch = get_branch(io_handler, db_handler)

		except Exception as e:
			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(branch)

