from django.http import JsonResponse
from django.http import QueryDict

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetCommunityDepartmentsIO:

	def __init__(self, request):

		self.request = request


	@property
	def community(self) -> str:

		try:

			return self.data.get('community')

		except Exception as e:
			# create exceptions (ParameterMissingFromRequest)
			print(e)


	@property
	def lang(self) -> str:

		try:
	
			return self.data.get('lang')

		except Exception as e:
			# create exceptions (ParameterMissingFromRequest)
			print(e)


	@property
	def scholar_year(self) -> str:

		try:
	
			return self.data.get('scholar_year')

		except Exception as e:
			# create exceptions (ParameterMissingFromRequest)
			print(e)
	

	def requestSerializer(self):

		self.data = QueryDict(self.request.META['QUERY_STRING'])


	def responseSerializer(self, community_departments):

		departments_list = []

		for department in community_departments:

			members_list = []
		
			for member in department.members:

				members_list.append({
					"name"  : member.name,
					"role" : member.role,
					"mail" : member.mail,
					"linkedin" : member.linkedin,
					"description" : member.description,
					"image" : member.image
					})

			departments_list.append({
				"name" : department.name,
				"members" : members_list
				})
		
		response = {"community_departments" : departments_list}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
