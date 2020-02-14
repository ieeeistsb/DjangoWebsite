from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from ..io import GetBranchIO

from ...usecases import get_branch

#from ..db import DBHandler
from ..mocks import MockDBHandler as DBHandler

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

