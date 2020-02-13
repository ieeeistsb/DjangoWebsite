from dataclasses import dataclass

from typing import List

@dataclass
class Event:

	__slots__ = '_name', '_date', '_description', '_image'

	_name : str
	_date : str
	_description : List[str]
	_image : str
	
	@property
	def name(self):
		return self._name

	@property
	def date(self):
		return self._date

	@property
	def description(self):
		return self._description

	@property
	def image(self):
		return self._image
	
	@classmethod
	def from_dict(cls, obj):
		return Event(obj['name'], obj['date'], obj['description'], obj['image'])

	def dict(self):
		return {
			'name': self.name,
			'date': self.date,
			'description' : self.description,
			'image': self.image
		}
