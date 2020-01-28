from .db import db
from dataclasses import dataclass
from typing import List, Any

from ...interfaces import DBInterface

from ...entities import Community


@dataclass
class MockDBHandler(DBInterface):

	__slots__ = 'request'
	request: Any
	communities = db.get('communities')

	def fetch_communities(self) -> List[Community]:

		return [Community(1, c.get('name')) for c in self.communities]
