from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import GetCommunitiesSerializer

from ...models   import CommunityModel
from ...entities import Community
from ...usecases import get_communities

class CommunitiesView(APIView):

	def get(self, request):
		ioSerializer = GetCommunitiesSerializer(request)
		ioSerializer.requestSerializer()

		try:
			#call usecase
			communities = get_communities()

		except Exception as e:
			return ioSerializer.errorSerializer(e)

		return ioSerializer.responseSerializer(communities)

