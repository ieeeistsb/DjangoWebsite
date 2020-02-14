from django.db import models
from typing import List

from ..entities import Member

from ..interfaces import DBInterface, GetCommunityDepartmentsIO

def get_community_departments(io_handler: GetCommunityDepartmentsIO, db_handler : DBInterface) -> List[Member]:
	
	try:

		lang = io_handler.lang
		community = io_handler.community

		community_departments = db_handler.fetch_community_departments(community, lang)

		return community_departments
	
	except Exception as e:
		print(e)
		raise e
