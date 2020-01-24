from dataclasses import dataclass

@dataclass
class Community:

	__slots__ = '_id', '_name'

	_id: int
	_name: str

	@property
	def id(self):
		return self._id
	
	@property
	def name(self):
		return self._name
	
	@classmethod
	def from_dict(cls, obj):
		return Community(obj['id'], obj['name'])

	def dict(self):
		return {
			'id': self.id,
			'name': self.name
		}
