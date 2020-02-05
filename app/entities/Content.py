from dataclasses import dataclass

@dataclass
class Content:

	__slots__ = '_id', '_pt', '_eng'

	_id  : str
	_pt  : str
	_eng : str

	@property
	def id(self):
		return self._id

	@property
	def pt(self):
		return self._pt

	@property
	def eng(self):
		return self._eng
	
	@classmethod
	def from_dict(cls, obj):
		return Content(obj['id'])

	def dict(self):
		return {
			'id'  : self.id,
			'pt'  : self.pt,
			'eng' : self.eng
		}
