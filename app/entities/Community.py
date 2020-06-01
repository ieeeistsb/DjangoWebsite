from dataclasses import dataclass

from typing import List, Any

from . import Page

@dataclass
class Community:

	__slots__ = '_name', '_tag', '_description', '_images', '_pages'

	_name : str
	_tag : str
	_description : List[str]
	_images : List[str]
	_pages : List[Any]
	
	@property
	def name(self):
		return self._name

	@property
	def tag(self):
		return self._tag

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
		return Community(obj['tag'], obj['name'], obj['description'], obj['images'], obj['pages'])

	def dict(self):
		return {
			'tag': self.tag,
			'name': self.name,
			'description': self.description,
			'images': self.images,
			'pages' : self.pages
		}
