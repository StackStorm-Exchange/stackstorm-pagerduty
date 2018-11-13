from lib.base import PdBaseAction

""" This action prepares data for base logic in lib/base.py
  Your action.yaml can reference find(), fetch(), delete(), and create() directly.
  Any other method will fall through to else, and be passed literally to lib/base.py.
  other methods should match up to a method in pypd.
"""


class PdAction(PdBaseAction):
    """ Pagerduty run action
    """

    def run(self, entity=None, method=None, **kwargs):
        """ Run action and call appropriate method
        """
        # Run a couple checks in PdBaseAction() to make sure global required
        # data is present
        self.check_entity(entity)
        self.check_method(method)
        # Other data validation checks are done in PdBaseAction() methods

        # Well known pypd methods in pypd.entity
        if method == 'find':  # HTTP_GET
            self.logger.debug('Running a find() method')

            return (True, self.find(entity=entity, **kwargs))

        elif method == 'fetch':  # HTTP_GET
            self.logger.debug('Running a fetch() method')

            # We need to know the id of the resource we are fetching.
            # Define 'entity_id' in your action
            entity_id = str(kwargs.pop('entity_id', None))
            self.logger.debug('Extracting entity_id from kwargs: {}'.format(entity_id))

            return (True, self.fetch(
                entity=entity, entity_id=entity_id, **kwargs))

        elif method == 'delete':  # HTTP_DELETE
            self.logger.debug('Running a delete() method')

            # We need to know the id of the resource we are deleting.
            # Define 'entity_id' in your action
            entity_id = str(kwargs.pop('entity_id', None))
            self.logger.debug('Extracting entity_id from kwargs: {}'.format(entity_id))

            return (True, self.delete(
                entity=entity, entity_id=entity_id, **kwargs))

        elif method == 'create':  # HTTP_POST
            self.logger.debug('Running a create() method')

            from_email = str(kwargs.pop('from_email', None))
            self.logger.debug('Extracting from_email from kwargs: {}'.format(from_email))

            # data should be a JSON object with a defined JSONschema in the
            # action to enforce API compliance.
            data = kwargs.pop('data', None)
            self.logger.debug('Extracting data from kwargs: {}'.format(data))

            return (True, self.create(
                entity=entity, from_email=from_email, payload=data, **kwargs))

        # If there ends up being a spcific method that needs some special handling
        # you can either add another `elif` condition here. You COULD create a
        # seperate `specfic_action.py` that instantiates PdBaseAction() directly,
        # but it's preferable for consistency to keep direct action logic here.

        # elif method == '<another>':
        # ...

        # other entity_id based methods
        else:
            self.logger.debug('Running an entity_id specific method')

            # We need to know the entity_id of the resource to interact with
            entity_id = str(kwargs.pop('entity_id', None))
            self.logger.debug(
                'Extracting entity_id from kwargs: {}'.format(entity_id))

            return (True, self.entity_id_method(
                entity=entity, method=method, entity_id=entity_id, **kwargs))
