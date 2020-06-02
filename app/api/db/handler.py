from dataclasses import dataclass
from typing import List, Any

from ...interfaces import DBInterface

from ...entities import Branch, Community, Department, Member, Page, Event

from .models import *


@dataclass
class DBHandler(DBInterface):
	
	__slots__ = 'request'
	request: Any

	def fetch_branch(self, lang : str, tag='IST') -> Branch:

		branch_model = BranchModel.objects.get(name=tag)

		return branch_model.toEntity(lang)

	def fetch_branch_events(self, lang : str, tag='IST') -> List[Any]:

		branch_model = BranchModel.objects.get(name=tag)

		events_models = branch_model.events()

		return [event.toEntity(lang) for event in events_models]

	
	def fetch_branch_departments(self, lang : str, scholar_year='19/20', tag='IST') -> List[Any]:

		branch_model = BranchModel.objects.get(name=tag)

		departments_models = branch_model.departments()

		return [department.toEntity(lang, scholar_year) for department in departments_models]

	def fetch_branch_images(self, tag='IST') -> List[str]:

		branch_model = BranchModel.objects.get(name=tag)

		images_models = branch_model.images()

		return [image.url() for image in images_models]

	def fetch_communities(self, lang : str) -> List[Any]:

		communities_models = CommunityModel.objects.all()

		return [community.toEntity(lang) for community in communities_models]

	def fetch_communities_events(self, lang : str) -> List[Any]:

		events = []

		communities_models = CommunityModel.objects.all()

		for community in communities_models:
			events += self.fetch_community_events(community.tag, lang)

		return events

	def fetch_community_events(self, community_tag : str, lang : str) -> List[Any]:

		community_model = CommunityModel.objects.get(tag=community_tag)

		events_models = community_model.events()

		return [event.toEntity(lang) for event in events_models]

	def fetch_community_departments(self, community_tag : str, lang : str, scholar_year='19/20') -> List[Any]:

		community_model = CommunityModel.objects.get(tag=community_tag)

		departments_models = community_model.departments()

		return [department.toEntity(lang, scholar_year) for department in departments_models]
