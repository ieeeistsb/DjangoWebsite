from django.db import models
from typing import List

from ..entities import Community
from ..models import CommunityModel

def get_communities() -> List[Community]:
	
	try:
		communities = [Community(c.id, c.name) for c in CommunityModel.objects.all()]
		return communities
	
	except Exception as e:
		print(e)
		raise e