from .db import db
from dataclasses import dataclass
from typing import List, Any

from ...interfaces import DBInterface

from ...entities import Community, Department, Event, Member, Page


@dataclass
class MockDBHandler(DBInterface):

	__slots__ = 'request'
	request: Any
	branch = db.get('branch')
	communities = db.get('communities')
	departments = db.get('departments')
	events = db.get('events')
	members = db.get('collaborators')
	content = db.get('content')
	pages = db.get('pages')


	def fetch_branch_departments(self, lang):

		departments = []

		for department_id in self.branch.get('departments'):

			departments.append(self.fetch_department(department_id, lang))

		return departments

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

	def fetch_community_events(self, community_tag, lang) -> List[Event]:

		events = []

		for community in self.communities:

			if community_tag == community.get('tag'):

				for event_id in community.get('events'):

					events.append(self.fetch_event(event_id, lang))

		return events

	def fetch_community_departments(self, community_tag, lang) -> List[Department]:

		departments = []

		for community in self.communities:

			if community_tag == community.get('tag'):

				for department_id in community.get('departments'):

					departments.append(self.fetch_department(department_id, lang))

		return departments


	def fetch_department(self, _id, lang) -> List[Department]:

		for department in self.departments:

			if department.get('id') == _id:

				members = []

				for member_id in department.get('members'):

					members.append(self.fetch_member(member_id, lang))

				return Department(department.get('name'), members)


	def fetch_page(self, page_type, lang) -> List[Page]:

		for page in self.pages:

			if page.get('type') == page_type:

				return Page(page_type, self.fetch_content(page.get('translatable_name'), lang))

	def fetch_content(self, _id, lang) -> str:

		for cont in self.content:

			if _id == cont.get('id'):

				return cont.get(lang)

	def fetch_event(self, _id, lang) -> Event:

		for event in self.events:

			if _id == event.get('id'):

				description = []

				for paragraph in event.get('description'):

					description.append(self.fetch_content(paragraph, lang))

				return Event(event.get('name'), event.get('date'), description, event.get('image'))

	def fetch_member(self, _id, lang) -> Member:

		for member in self.members:

			if _id == member.get('id'):

				description = []

				for paragraph in member.get('description'):

					description.append(self.fetch_content(paragraph, lang))

				return Member(member.get('name'), member.get('contact'), description, member.get('image'))
