from django.db import models
from typing import List

from ..entities import Event

from ..interfaces import DBInterface, GetBranchEventsIO

def get_branch_events(io_handler: GetBranchEventsIO, db_handler : DBInterface) -> List[Event]:
	
	try:

		lang = io_handler.lang

		branch_events = db_handler.fetch_branch_events(lang)

		return branch_events
	
	except Exception as e:
		print(e)
		raise e
