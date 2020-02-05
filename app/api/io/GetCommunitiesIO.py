from django.http import JsonResponse

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetCommunitiesIO:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		#data = json.loads(self.request.body)
		pass

	def responseSerializer(self, communities):

		communities_list = []
		
		for c in communities:
			pages = [{
					"type" : p.name,
					"name" : p.name
				} for p in c.pages]

			communities_list.append({
				"name" : c.name,
				"tag" : c.tag,
				"pages" : pages
				})
		
		response = {"communities" : communities_list}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
