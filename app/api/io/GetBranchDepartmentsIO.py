from django.http import JsonResponse
from django.http import QueryDict

# import entity
from rest_framework.response import Response
from rest_framework import status

import json

class GetBranchDepartmentsIO:

	def __init__(self, request):

		self.request = request

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


	def responseSerializer(self, branch_departments):

		departments_list = []

		for department in branch_departments:

			members_list = []
		
			for member in department.members:

				members_list.append({
					"name"  : member.name,
					"mail" : member.mail,
					"role" : member.role,
					"linkedin" : member.linkedin,
					"description" : member.description,
					"image" : member.image
					})

			departments_list.append({
				"name" : department.name,
				"members" : members_list
				})
		
		response = {"branch_departments" : departments_list}
		
		return JsonResponse(response)

	def errorSerializer(self, error):
		return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
