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

        # Well known pypd methods in pypd.entity

        if method == 'find':  # HTTP_GET
            return (True, self.find(entity=entity, **kwargs))

        elif method == 'fetch':  # HTTP_GET
            # We need to know the id of the resource we are fetching. Define 'entity_id' in
            # your action
            if not kwargs.get('entity_id', None):
                return (False, "entity_id is a required field. Needed for pypd.entity.fetch()")
            entity_id = str(kwargs.pop('entity_id'))

            return (True, self.fetch(entity=entity, entity_id=entity_id, **kwargs))

        elif method == 'delete':  # HTTP_DELETE
            # We need to know the id of the resource we are deleting. Define 'entity_id' in
            # your action
            if not kwargs.get('entity_id', None):
                return (False, "entity_id is a required field. Needed for pypd.entity.delete()")
            entity_id = str(kwargs.pop('entity_id'))

            return (True, self.delete(entity=entity, entity_id=entity_id, **kwargs))

        elif method == 'create':  # HTTP_POST
            # We need to know the email of the user making the resource
            if not kwargs.get('from_email', None):
                return (False, "from_email is a required field. Needed for pypd.entity.create()")
            from_email = str(kwargs.pop('from_email'))

            # data should be a JSON object with a defined JSONschema in the action to enforce API compliance.
            if not kwargs.get('data', None):
                return (False, "entity_id is a required field. Needed for pypd.entity.create()")
            data = kwargs.pop('data')

            return (True, self.create(entity=entity, from_email=from_email, payload=data, **kwargs))

        # other id based methods
        else:
            # check for required fields
            if not kwargs.get('entity_id', None):
                return (False, "entity_id is a required field. Needed for %s operations" % method)
            entity_id = str(kwargs.pop('entity_id'))

            # if kwargs.get('_id', None):
            #     kwargs['id'] = str(kwargs.pop('_id'))
                # See note in lib/base/py on why this is happening.

            return (True, self.entity_id_method(entity=entity, method=method, entity_id=entity_id, **kwargs))
