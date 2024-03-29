from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from ..io import GetBranchBooksIO

from ...usecases import get_branch_books

if settings.MOCK_DB:
	from ..mocks import MockDBHandler as DBHandler
else:
	from ..db import DBHandler

class BranchBooksView(APIView):

	def get(self, request):

		io_handler = GetBranchBooksIO(request)
		db_handler = DBHandler(request)

		io_handler.requestSerializer()

		try:

			branch_books = get_branch_books(io_handler, db_handler)

		except Exception as e:

			return io_handler.errorSerializer(e)

		return io_handler.responseSerializer(branch_books)
