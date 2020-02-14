from django.db import models
from typing import List

from ..entities import Community

from ..interfaces import DBInterface, GetBranchIO

def get_branch(io_handler : GetBranchIO, db_handler : DBInterface) -> List[Community]:
	
	try:

		lang = io_handler.lang

		branch = db_handler.fetch_branch(lang)

		return branch
	
	except Exception as e:
		print(e)
		raise e
