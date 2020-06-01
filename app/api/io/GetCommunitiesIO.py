from django.http import JsonResponse
from django.http import QueryDict

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetCommunitiesIO:

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


	def responseSerializer(self, communities):

		communities_list = []
		
		for c in communities:
			pages = [{
					"type" : p.type,
					"name" : p.name
				} for p in c.pages]

			communities_list.append({
				"name" : c.name,
				"tag" : c.tag,
				"description": c.description,
				"images": c.images,
				"pages" : pages
				})
		
		response = {"communities" : communities_list}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
