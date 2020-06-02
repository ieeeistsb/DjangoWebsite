from django.db import models
from typing import List

from ..entities import Branch

from ..interfaces import DBInterface, GetBranchImagesIO

def get_branch_images(io_handler : GetBranchImagesIO, db_handler : DBInterface) -> List[str]:
	
	try:

		images = db_handler.fetch_branch_images()

		return images
	
	except Exception as e:
		print(e)
		raise e
