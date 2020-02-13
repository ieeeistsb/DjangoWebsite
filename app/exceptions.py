
class ParameterMissingFromRequest(Exception):

	def __init__(self, parameter):

		super().__init__(f'Parameter ({parameter}) is missing')
		