from dataclasses import dataclass

@dataclass
class Page:

	__slots__ = '_type', '_name'

	_type : str
	_name : str

	@property
	def type(self):
		return self._type

	@property
	def name(self):
		return self._name
	
	@classmethod
	def from_dict(cls, obj):
		return Page(obj['type'], obj['name'])

	def dict(self):
		return {
			'type': self.type,
			'name' : self.name
		}
