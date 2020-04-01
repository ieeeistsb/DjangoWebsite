from django.db import models
from typing import List

from ..entities import Branch

from ..interfaces import DBInterface, GetBranchIO

def get_branch(io_handler : GetBranchIO, db_handler : DBInterface) -> Branch:
	
	try:

		lang = io_handler.lang

		branch = db_handler.fetch_branch(lang)

		return branch
	
	except Exception as e:
		print(e)
		raise e
