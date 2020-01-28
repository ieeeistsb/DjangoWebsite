from django.db import models
from typing import List

from ..entities import Community

from ..interfaces import DBInterface

def get_communities(db_handler : DBInterface) -> List[Community]:
	
	try:
		communities = db_handler.fetch_communities()
		return communities
	
	except Exception as e:
		print(e)
		raise e