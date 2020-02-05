
from typing import List
from .entities import Community, Page

class DBInterface(object):
	__slots__ = tuple()

	def fetch_communities(self) -> List[Community]:
		raise NotImplementedError('Method `async def fetch_communities(self) -> List[Community]` must be implemented')

	def fetch_page(self, page_type) -> List[Page]:
		raise NotImplementedError('Method `async def fetch_page(self, page_type) -> List[Page]` must be implemented')
