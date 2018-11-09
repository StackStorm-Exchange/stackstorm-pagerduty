from lib.base import PdBaseAction


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
			#We need to know the id of the resource we are fetching. Define 'resource_id' in your action
			if not kwargs.get('resource_id', None):
				return (False, "resource_id is a required field for fetch()")
			resource_id = str(kwargs.pop('resource_id'))
			return (True, self.fetch(entity=entity, _id=resource_id, **kwargs))

		elif method == 'find':
			return (True, self.find(entity=entity, **kwargs))

		elif method == 'create':
			#We need to know the email of the user making the resource
			if not kwargs.get('from_email', None):
				return (False, "from_email is a required field for create()")
			from_email = str(kwargs.pop('from_email'))
			return (True, self.create(entity=entity, from_email=from_email, **kwargs))

		elif method == 'delete':
			#We need to know the id of the resource we are deleting. Define 'resource_id' in your action
			if not kwargs.get('resource_id', None):
				return (False, "resource_id is a required field for delete()")
			resource_id = str(kwargs.pop('resource_id'))
			return (True, self.delete(entity=entity, _id=resource_id, **kwargs))

#Next up... Variable methods!
		# else:
		# 	#many entities have custom methods that require specific fields, if 'id' is significant, pass 'resource_id' and it will be handled
		# 	return (True, self.other(entity=entity, method=method, **kwargs))
