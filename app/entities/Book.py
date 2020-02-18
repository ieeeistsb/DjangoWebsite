from dataclasses import dataclass

from typing import List, Any

@dataclass
class Book:

	__slots__ = '_title', '_author', '_year_edition', '_price', '_quality', '_contact', '_image'

	_title : str
	_author : str
	_year_edition : str
	_price : str
	_quality : str
	_contact : str
	_image : str
	
	@property
	def title(self):
		return self._title

	@property
	def author(self):
		return self._author

	@property
	def year_edition(self):
		return self._year_edition
	
	@property
	def price(self):
		return self._price
	
	@property
	def quality(self):
		return self._quality
	
	@property
	def contact(self):
		return self._contact
	
	@property
	def image(self):
		return self._image
	
	@classmethod
	def from_dict(cls, obj):
		return Book(obj['title'], obj['author'], obj['year_edition'], obj['price'], obj['quality'], obj['contact'], obj['image'])

	def dict(self):
		return {
			'title' : self.title,
			'author' : self.author,
			'year_edition' : self.year_edition,
			'price' : self.price,
			'quality' : self.quality,
			'contact' : self.contact,
			'image' : self.image
		}
