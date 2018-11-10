import pypd
import json

from st2common.runners.base_action import Action


class PdBaseAction(Action):
    """ Base Pagerduty class for all actions
    """
    # if entity is None:
    #     raise InvalidArguments(entity)

    def __init__(self, config):
        """ init method, run at class creation
        """
        super(PdBaseAction, self).__init__(config)
        self.pd = self._init_client()

    def _init_client(self):
        """ init_client method, run at class creation
        """
        pypd.api_key = self.config['api_key']
        pypd.service_key = self.config['service_key']
        return pypd

    def fetch(self, entity=None, user_id=None, **kwargs):
        """ base fetch() method defined in pypd.entity.fetch() usable by most entities
        """
        if user_id is None:
            raise InvalidArguments(user_id)
        fetch = getattr(self.pd, entity).fetch(id=user_id, **kwargs)
        # use pypd method entity.json to return the entity as json
        return fetch.json

    def find(self, entity=None, **kwargs):
        """ base find() method defined in pypd.entity.find() usable by all entities
        """
        if 'maximum' not in kwargs:
            # if maximum was ommited from the action, or didn't have a default,
            # make sure we don't have a rediculous response
            kwargs['maximum'] = 25

        find = getattr(self.pd, entity).find(**kwargs)
        found = []
        for f in find:
            found.append(f.json)

        # use pypd method entity.json to return the entity as json
        return found

    def delete(self, entity=None, user_id=None, **kwargs):
        """ base delete() method defined in pypd.entity.delete() usable by most entities
        """
        if user_id is None:
            raise InvalidArguments(user_id)
        delete = getattr(self.pd, entity).delete(id=user_id, **kwargs)
        if delete is True:
            return json.loads('{"deleted":true}')
        else:
            # use pypd method entity.json to return the entity as json
            return delete.json

    def create(self, entity=None, from_email=None, payload=None, **kwargs):
        """ base create() method defined in pypd.entity.create() usable by most entities
        """
        if from_email is None:
            raise InvalidArguments(from_email)
        if payload is None:
            raise InvalidArguments(payload)

        create = getattr(self.pd, entity).create(
            data=payload, from_email=from_email, **kwargs)
        # use pypd method entity.json to return the entity as json
        return create.json

    def user_id_method(self, entity=None, method=None, user_id=None, **kwargs):
        """ base method to handle other methods that depend on an `id` for a user

            Make sure to use the PD API reference to determine if your action needs a `from` (use action parameter `from_email`)

            If the method has a secondary id for a resource attached to a parent id (user.id vs user.id.notification_rule.id)
            it can't be sent as the proper name referenced in the API. pypd decided that instead of just accepting `user.id` and `secondary.id`
            you must first instantiate `user.id` and then call the method as `user.method(secondary.id)`
            For this reason secondary id needs to be passed as `resource_id` so that we can rewrite the `resource_id` key to `id`
            and have it pass through with kwargs as "id=<value>"
            This is all obviously less than ideal, but at this point requres a pypd rewrite, or this pack to be rewritten
            to not need pypd and use custom rest client. (maybe the next major version?)

            If you need to send a payload, it should be a JSON string with the keys and values as defined from the PD API reference
            All the examples will have one extra top level key that should be omitted due to differences between the API and pypd
            For example, in Teams/put_teamsuser_id the payload ('team') example is
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

        # check for required fields
        if not user_id:
            raise InvalidArguments(user_id)
        # if there is a specific ID for the method being called, it should be passed as `resource_id` and we
        # will change it to `id` which is what pypd expects.
        if kwargs.get('resource_id', None):
            kwargs['id'] = kwargs.pop('resource_id')

        source = getattr(self.pd, entity).fetch(id=user_id)
        user_id_method = getattr(source, method)(**kwargs)

        # use pypd method entity.json to return the entity as json
        return user_id_method
