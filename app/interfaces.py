
from typing import List
from .entities import Community

class DBInterface(object):
	__slots__ = tuple()

	def fetch_communities(self) -> List[Community]:
		raise NotImplementedError('Method `async def get_communities(self) -> List[Community]` must be implemented')

