import pypd
import json

from st2common.runners.base_action import Action


class PdBaseAction(Action):
    """ Base Pagerduty class for all actions
    """

    def __init__(self, config):
        """ init method, run at class creation
        """
        super(PdBaseAction, self).__init__(config)
        self.logger.debug('Instantiating PdBaseAction()')
        self.pd = self._init_client()

    def _init_client(self):
        """ init_client method, run at class creation
        """
        self.logger.debug('Initializing pypd client')
        pypd.api_key = self.config['api_key']
        pypd.service_key = self.config['service_key']
        return pypd

    def fetch(self, entity=None, entity_id=None, **kwargs):
        """ base fetch() method defined in pypd.entity.fetch() usable by most entities
        """
        check_inputs = {}  # Placeholder for input checking
        check_inputs['entity_id'] = entity_id
        self.check_required(check_inputs)

        self.logger.debug('Running pypd fetch() for entity {}'.format(entity))
        fetch = getattr(self.pd, entity).fetch(id=entity_id, **kwargs)
        self.logger.debug('pypd find() finished')
        # use pypd method entity.json to return the entity as json
        return fetch.json

    def find(self, entity=None, **kwargs):
        """ base find() method defined in pypd.entity.find() usable by all entities
        """
        if 'maximum' not in kwargs:
            # if maximum was ommited from the action, or didn't have a default,
            # make sure we don't have a rediculously large response
            kwargs['maximum'] = 25
            self.logger.debug(
                'No maximum set for find(). Setting "maximum=25 to limit response size')

        self.logger.debug('Running pypd find() for entity {}'.format(entity))
        find = getattr(self.pd, entity).find(**kwargs)
        self.logger.debug('pypd find() finished')
        found = []
        for f in find:
            found.append(f.json)

        # use pypd method entity.json to return the entity as json
        return found

    def delete(self, entity=None, entity_id=None, **kwargs):
        """ base delete() method defined in pypd.entity.delete() usable by most entities
        """
        check_inputs = {}  # Placeholder for input checking
        check_inputs['entity_id'] = entity_id
        self.check_required(check_inputs)

        self.logger.debug('Running pypd delete() for entity {}'.format(entity))
        delete = getattr(self.pd, entity).delete(id=entity_id, **kwargs)
        self.logger.debug('pypd delete() finished')
        if delete is True:
            return json.loads('{"deleted":true}')
        else:
            # use pypd method entity.json to return the entity as json
            return delete.json

    def create(self, entity=None, from_email=None, payload=None, **kwargs):
        """ base create() method defined in pypd.entity.create() usable by most entities
        """
        check_inputs = {}  # Placeholder for input checking
        # We need to know the email of the user making the resource
        # and that a payload (data) is present
        check_inputs['from_email'] = from_email
        check_inputs['payload'] = payload
        self.check_required(check_inputs)

        """ Beacuse of inconsistencies with the pypd pack in how it handles data, we 
            must duplicate 'from_email' as 'from' because sometimes it's one or the other.
            It's not great, but we have to send it as both.
            See Incident.create Vs User.create in pypd
            
            Pagerduty's API literally requires the well known HTTP header field 'From'
            https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
        """
        kwargs['add_headers'] = ('{"from": "%s"}' % from_email)

        self.logger.debug('Running pypd create() for entity {}'.format(entity))
        create = getattr(self.pd, entity).create(
            data=payload, from_email=from_email, **kwargs)

        self.logger.debug('pypd create() finished')
        # use pypd method entity.json to return the entity as json
        return create.json

    def entity_id_method(self, entity=None, method=None, entity_id=None, **kwargs):
        """ base method to handle other methods that depend on an `id` for a user

            Make sure to use the PD API reference to determine if your action 
            needs a `from` (use action parameter `from_email`)

            If the method has a secondary id for a resource attached to a parent id
            (user.id vs user.id.notification_rule.id) it can't be sent as the proper name
            referenced in the API. pypd decided that instead of just accepting `user.id` 
            and `secondary.id` you must first instantiate `user.id` and then call the method
            as `user.method(secondary.id)`. For this reason secondary id needs to be passed
            as `resource_id` so that we can rewrite the `resource_id` key to `id` and have 
            it pass through with kwargs as "id=<value>". This is all obviously less than 
            ideal, but at this point requres a pypd rewrite, or this pack to be rewritten
            to not need pypd and use custom rest client. (maybe the next major version?)

            If you need to send a payload, it should be a JSON string with the keys and 
            values as defined from the PD API reference. All the examples will have one 
            extra top level key that should be omitted due to differences between the 
            API and pypd. For example, in Teams/post_teams the payload ('team') 
            example is
                {
                  "team": {
                    "type": "team",
                    "name": "Engineering",
                    "description": "The engineering team"
                  }
                }
            Where as the actual payload should be
                {
                    "type": "team",
                    "name": "Engineering",
                    "description": "The engineering team"
                }
        """

        # add required fields to be checked
        check_inputs = {}  # Placeholder for input checking
        check_inputs['entity_id'] = entity_id

        # if there is a specific ID for the method being called, it should be passed as
        # `resource_id` and we will change it to `id` which is what pypd expects.
        if kwargs.get('resource_id', None):
            check_inputs['resource_id'] = kwargs.get('resource_id', None)
            kwargs['id'] = kwargs.pop('resource_id', None)

        # check for required fields
        self.check_required(check_inputs)

        # We have to create an object to be referenced by the method.
        # This is how pypd is designed to work
        self.logger.debug('running a fetch() on {}:{}'.format(entity, entity_id))
        source = getattr(self.pd, entity).fetch(id=entity_id)
        # Call the method based on the entity object and pass any kwargs
        self.logger.debug('Running pypd {} on {}:{}'.format(method, entity, entity_id))
        entity_id_method = getattr(source, method)(**kwargs)

        # delete methods based on a user id will return null/None when successful.
        # Add useful output consistent with delete()
        if entity_id_method is None:
            self.logger.debug(
                'Delete operation successful. (response from pypd was None)')
            return json.loads('{"deleted":true}')

        # use pypd method entity.json to return the entity as json
        return entity_id_method

    def check_entity(self, entity=None):
        self.logger.debug('Checking if entity is defined')
        if entity is None:
            self.logger.error(
                'entity is a required field for all operations and was not found. Exiting...')
            exit(1)
        return True

    def check_method(self, method=None):
        self.logger.debug('Checking if method is defined')
        if method is None:
            self.logger.error(
                'method is a required field for all operations and was not found. Exiting...')
            exit(1)
        return True

    def check_required(self, check=None):
        """ Evaluate all the keys in the dict 'check' to ensure it exists and 
            if it is None, raise errors, log, and exit.
        """
        self.logger.debug(
            'running check_required(); inputs: {}'.format(check))
        if check is None:
            self.logger.error(
                'Required fields missing (None received); check_required()')
            exit(1)

        for k, v in check.iteritems():
            if v is None:
                self.logger.error(
                    '{} is a required field; check_required()'.format(k))
                exit(1)
        return True
