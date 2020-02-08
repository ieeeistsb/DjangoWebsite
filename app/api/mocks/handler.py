from .db import db
from dataclasses import dataclass
from typing import List, Any

from ...interfaces import DBInterface

from ...entities import Community, Page


@dataclass
class MockDBHandler(DBInterface):

	__slots__ = 'request'
	request: Any
	communities = db.get('communities')
	content = db.get('content')
	pages = db.get('pages')

	def fetch_communities(self, lang) -> List[Community]:

		communities = []

		for community in self.communities:

			pages = []

			for page_type in community.get('pages'):

				pages.append(self.fetch_page(page_type, lang))

			description = []

			for paragraph in community.get('description'):

				description.append(self.fetch_content(paragraph, lang))

			communities.append(Community(community.get('name'), community.get('tag'), description, pages))

		return communities

	def fetch_page(self, page_type, lang) -> List[Page]:

		for page in self.pages:

			if page.get('type') == page_type:

				return Page(page_type, self.fetch_content(page.get('translatable_name'), lang))

	def fetch_content(self, _id, lang) -> str:

		for cont in self.content:

			if _id == cont.get('id'):

				return cont.get(lang)
