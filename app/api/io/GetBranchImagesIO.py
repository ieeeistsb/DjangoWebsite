from django.http import JsonResponse
from django.http import QueryDict

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetBranchImagesIO:

	def __init__(self, request):

		self.request = request
	

	def requestSerializer(self):

		pass		

	def responseSerializer(self, branch_images):
		
		response = {"branch_images" : branch_images}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
