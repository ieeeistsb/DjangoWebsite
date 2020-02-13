from django.db import models
from typing import List

from ..entities import Event

from ..interfaces import DBInterface, GetCommunityEventsIO

def get_community_events(io_handler: GetCommunityEventsIO, db_handler : DBInterface) -> List[Event]:
	
	try:

		lang = io_handler.lang
		community = io_handler.community

		community_events = db_handler.fetch_community_events(community, lang)

		return community_events
	
	except Exception as e:
		print(e)
		raise e
