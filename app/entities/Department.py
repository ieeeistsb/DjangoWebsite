from dataclasses import dataclass

from typing import List, Any


@dataclass
class Department:

	__slots__ = '_name', '_members'

	_name : str
	_members : List[Any]
	
	@property
	def name(self):
		return self._name

	@property
	def members(self):
		return self._members
	
	@classmethod
	def from_dict(cls, obj):
		return Department(obj['name'], obj['members'])

	def dict(self):
		return {
			'name' : self.name,
			'members' : self.members
		}
