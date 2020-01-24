from django.http import JsonResponse

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetCommunitiesSerializer:

	def __init__(self, request):
		self.request = request

	def requestSerializer(self):
		#data = json.loads(self.request.body)
		pass

	def responseSerializer(self, communities):

		communities_list = []
		
		for c in communities:
			communities_list.append({
				"name" : c.name,
				"pages" : ["members", "about"]
				})
		
		response = str(communities_list)
		
		return Response(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
