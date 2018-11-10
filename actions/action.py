from lib.base import PdBaseAction

""" This action can be used as a shortcut for the methods .fetch() .find() and .delete()
	They follow a strict set of logic that is easily repeatable.
"""

class PdAction(PdBaseAction):
	""" Pagerduty run action
	"""
	def run(self, entity=None, method=None, **kwargs):
		""" run action and call appropriate method
		"""

		if entity is None:
			return (False, "entity is a required field")
		if method is None:
			return (False, "method is a required field")

		#Well known pypd methods in pypd.entity
		if method == 'fetch':
			#We need to know the id of the resource we are fetching. Define '_id' in your action
			if not kwargs.get('_id', None):
				return (False, "_id is a required field for fetch()")
			_id = str(kwargs.pop('_id'))
			return (True, self.fetch(entity=entity, _id=_id, **kwargs))

		elif method == 'find':
			return (True, self.find(entity=entity, **kwargs))

		elif method == 'delete':
			#We need to know the id of the resource we are deleting. Define '_id' in your action
			if not kwargs.get('_id', None):
				return (False, "_id is a required field for delete()")
			_id = str(kwargs.pop('_id'))
			return (True, self.delete(entity=entity, id=_id, **kwargs))

		elif method == 'create':
			#We need to know the email of the user making the resource
			if not kwargs.get('from_email', None):
				return (False, "from_email is a required field for create()")
			if not kwargs.get('data', None):
				return (False, "_id is a required field for fetch()")

			#data should be 
			data = str(kwargs.pop('data'))
			from_email = str(kwargs.pop('from_email'))
			return (True, self.create(entity=entity, from_email=from_email, payload=data, **kwargs))		

		#other post and put based methods
			