from dataclasses import dataclass
from typing import List, Any

from ...interfaces import DBInterface

from ...entities import Community

from .models import CommunityModel


@dataclass
class DBHandler(DBInterface):
	
	__slots__ = 'request'
	request: Any

	def fetch_communities(self) -> List[Community]:

		return [Community(c.id, c.name) for c in CommunityModel.objects.all()]
