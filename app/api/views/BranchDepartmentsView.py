from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from ..io import GetBranchDepartmentsIO

from ...usecases import get_branch_departments

from ..db import DBHandler
#from ..mocks import MockDBHandler as DBHandler

class BranchDepartmentsView(APIView):

	def get(self, request):

		io_handler = GetBranchDepartmentsIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:

			branch_departments = get_branch_departments(io_handler, db_handler)

		except Exception as e:

			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(branch_departments)
