from dataclasses import dataclass

from .SocialNetwork import SocialNetwork

from typing import List

@dataclass
class Volunteer:

	__slots__ = '_id', '_name', '_email', '_socials', '_image'

	_id: int
	_name: str
	_email: str
	_socials: List[SocialNetwork]
	_image: str

	@property
	def id(self):
		return self._id
	
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, email):
		self._email = email

	@property
	def socials(self):
		return self._socials

	@socials.setter
	def socials(self, socials):
		self._socials
	
	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image
	
	@classmethod
	def from_dict(cls, obj):
		return Volunteer(obj['id'], obj['name'], obj)

	def dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email,
			'socials': self.socials,
			'image': self.image
		}
