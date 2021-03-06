
from typing import List
from .entities import Branch, Community, Department, Event, Member, Page, Book

class DBInterface(object):
	__slots__ = tuple()

	def fetch_branch(self, lang) -> Branch:
		raise NotImplementedError('Method `def fetch_branch(self, lang) -> Branch` must be implemented')

	def fetch_branch_departments(self, lang) -> List[Department]:
		raise NotImplementedError('Method `def fetch_branch_departments(self, lang) -> List[Department]` must be implemented')

	def fetch_branch_events(self, lang) -> List[Event]:
		raise NotImplementedError('Method `def fetch_branch_events(self, lang) -> List[Event]` must be implemented')

	def fetch_branch_images(self, tag='IST') -> List[str]:
		raise NotImplementedError('Method `def fetch_branch_images(self, tag) -> List[str]` must be implemented')

	def fetch_branch_books(self, lang) -> List[Book]:
		raise NotImplementedError('Method `def fetch_branch_books(self, lang) -> List[Book]` must be implemented')

	def fetch_communities(self, lang) -> List[Community]:
		raise NotImplementedError('Method `def fetch_communities(self, lang) -> List[Community]` must be implemented')

	def fetch_communities_events(self, lang) -> List[Event]:
		raise NotImplementedError('Method `def fetch_communities_events(self, lang) -> List[Event]` must be implemented')

	def fetch_community_events(self, community_tag, lang) -> List[Event]:
		raise NotImplementedError('Method `def fetch_community_events(self, community_tag, lang) -> List[Event]` must be implemented')

	def fetch_community_departments(self, community_tag, lang) -> List[Department]:
		raise NotImplementedError('Method `def fetch_community_members(self, community_tag, lang) -> List[Department]` must be implemented')

	def fetch_page(self, page_type) -> List[Page]:
		raise NotImplementedError('Method `def fetch_page(self, page_type) -> List[Page]` must be implemented')


class GetBranchIO(object):
	__slots__ = tuple()

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, branch):
		raise NotImplementedError('Method `def responseSerializer(self, branch) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetBranchDepartmentsIO(object):
	__slots__ = tuple()

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, branch_departments):
		raise NotImplementedError('Method `def responseSerializer(self, branch_departments) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetBranchEventsIO(object):
	__slots__ = tuple()

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, branch_events):
		raise NotImplementedError('Method `def responseSerializer(self, branch_events) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetBranchImagesIO(object):
	__slots__ = tuple()
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, branch_images):
		raise NotImplementedError('Method `def responseSerializer(self, branch_events) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetBranchBooksIO(object):
	__slots__ = tuple()

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, branch_books):
		raise NotImplementedError('Method `def responseSerializer(self, branch_books) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetCommunitiesIO(object):
	__slots__ = tuple()

	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, communities):
		raise NotImplementedError('Method `def responseSerializer(self, communities) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetCommunityEventsIO(object):
	__slots__ = tuple()

	@property
	def community(self) -> str:
		raise NotImplementedError('Property `def community(self) -> str` must be implemented')

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, community_events):
		raise NotImplementedError('Method `def responseSerializer(self, community_events) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')


class GetCommunityDepartmentsIO(object):
	__slots__ = tuple()

	@property
	def community(self) -> str:
		raise NotImplementedError('Property `def community(self) -> str` must be implemented')

	@property
	def lang(self) -> str:
		raise NotImplementedError('Property `def lang(self) -> str` must be implemented')
	
	def requestSerializer(self):
		raise NotImplementedError('Method `def requestSerializer(self) -> ` must be implemented')

	def responseSerializer(self, community_departments):
		raise NotImplementedError('Method `def responseSerializer(self, community_departments) -> ` must be implemented')

	def errorSerializer(self, error):
		raise NotImplementedError('Method `def errorSerializer(self) -> ` must be implemented')