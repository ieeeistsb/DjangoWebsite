from django.http import JsonResponse
from django.http import QueryDict

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetBranchEventsIO:

	def __init__(self, request):

		self.request = request

	@property
	def lang(self) -> str:

		try:
	
			return self.data.get('lang')

		except Exception as e:
			# create exceptions (ParameterMissingFromRequest)
			print(e)
	

	def requestSerializer(self):

		self.data = QueryDict(self.request.META['QUERY_STRING'])


	def responseSerializer(self, branch_events):

		events_list = []

		for event in branch_events:

			events_list.append({
				"name"  : event.name,
				"date"  : event.date,
				"description" : event.description,
				"image" : event.image
				})
		
		response = {"branch_events" : events_list}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
