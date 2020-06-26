from dataclasses import dataclass

from typing import List

@dataclass
class Member:

	__slots__ = '_name', '_role', '_mail', '_linkedin', '_description', '_image'

	_name : str
	_role : str
	_mail : str
	_linkedin : str
	_description : List[str]
	_image : str
	
	@property
	def name(self):
		return self._name

	@property
	def role(self):
		return self._role

	@property
	def mail(self):
		return self._mail

	@property
	def linkedin(self):
		return self._linkedin
	
	@property
	def description(self):
		return self._description

	@property
	def image(self):
		return self._image
	
	@classmethod
	def from_dict(cls, obj):
		return Member(obj['name'], obj['role'], obj['mail'], obj['linkedin'], obj['description'], obj['image'])

	def dict(self):
		return {
			'name' : self.name,
			'role' : self.role,
			'mail' : self.mail,
			'linkedin' : self.linkedin,
			'description' : self.description,
			'image': self.image
		}
