from dataclasses import dataclass

from typing import List

@dataclass
class Member:

	__slots__ = '_name', '_contact', '_description', '_image'

	_name : str
	_contact : str
	_description : List[str]
	_image : str
	
	@property
	def name(self):
		return self._name

	@property
	def contact(self):
		return self._contact
	
	@property
	def description(self):
		return self._description

	@property
	def image(self):
		return self._image
	
	@classmethod
	def from_dict(cls, obj):
		return Member(obj['name'], obj['contact'], obj['description'], obj['image'])

	def dict(self):
		return {
			'name' : self.name,
			'contact' : self.contact,
			'description' : self.description,
			'image': self.image
		}
