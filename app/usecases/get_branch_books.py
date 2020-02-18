from django.db import models
from typing import List

from ..entities import Book

from ..interfaces import DBInterface, GetBranchBooksIO

def get_branch_books(io_handler: GetBranchBooksIO, db_handler : DBInterface) -> List[Book]:
	
	try:

		lang = io_handler.lang

		branch_books = db_handler.fetch_branch_books(lang)

		return branch_books
	
	except Exception as e:
		print(e)
		raise e
