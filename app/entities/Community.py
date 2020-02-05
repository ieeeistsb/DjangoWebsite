from dataclasses import dataclass

from typing import List, Any

from . import Page

@dataclass
class Community:

	__slots__ = '_name', '_tag', '_pages'

	_name : str
	_tag : str
	_pages : List[Any]
	
	@property
	def name(self):
		return self._name

	@property
	def tag(self):
		return self._tag

	@property
	def pages(self):
		return self._pages
	
	@classmethod
	def from_dict(cls, obj):
		return Community(obj['id'], obj['name'], obj['pages'])

	def dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'pages' : self.pages
		}
