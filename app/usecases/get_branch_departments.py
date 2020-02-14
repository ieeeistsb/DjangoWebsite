from django.db import models
from typing import List

from ..entities import Member

from ..interfaces import DBInterface, GetBranchDepartmentsIO

def get_branch_departments(io_handler: GetBranchDepartmentsIO, db_handler : DBInterface) -> List[Member]:
	
	try:

		lang = io_handler.lang

		branch_departments = db_handler.fetch_branch_departments(lang)

		return branch_departments
	
	except Exception as e:
		print(e)
		raise e
