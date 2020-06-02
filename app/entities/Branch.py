from dataclasses import dataclass

from typing import List, Any

from . import Page

@dataclass
class Branch:

	__slots__ = '_name', '_description', '_images', '_pages'

	_name : str
	_description : List[str]
	_images : List[str]
	_pages : List[Any]
	
	@property
	def name(self):
		return self._name

	@property
	def description(self):
		return self._description
	
	@property
	def images(self):
		return self._images

	@property
	def pages(self):
		return self._pages
	
	@classmethod
	def from_dict(cls, obj):
		return Branch(obj['name'], obj['description'], obj['images'], obj['pages'])

	def dict(self):
		return {
			'name': self.name,
			'description': self.description,
			'images' : self.images,
			'pages' : self.pages
		}
