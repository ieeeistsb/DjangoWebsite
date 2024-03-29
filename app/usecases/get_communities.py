from django.db import models
from typing import List

from ..entities import Community

from ..interfaces import DBInterface, GetBranchIO

def get_communities(io_handler : GetBranchIO, db_handler : DBInterface) -> List[Community]:
	
	try:

		lang = io_handler.lang

		communities = db_handler.fetch_communities(lang)

		return communities
	
	except Exception as e:
		print(e)
		raise e
