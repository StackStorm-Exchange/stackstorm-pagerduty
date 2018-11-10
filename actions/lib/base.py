import pypd
import json

from st2common.runners.base_action import Action


class PdBaseAction(Action):
    """ Base Pagerduty class for all actions
    """
    if entity is None:
        raise InvalidArguments(entity)

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


    def fetch(self, entity=None, _id=None, **kwargs):
        """ base fetch() method defined in pypd.entity.fetch() usable by most entities
        """
        if _id is None:
            raise InvalidArguments(_id)
        fetch = getattr(self.pd, entity).fetch(id=_id, **kwargs)
        #use pypd method entity.json to return the entity as json
        return fetch.json


    def find(self, entity=None, **kwargs):
        """ base find() method defined in pypd.entity.find() usable by all entities
        """
        if not 'maximum' in kwargs:
            #if maximum was ommited from the action, or didn't have a default, make sure we don't have a rediculous response
            kwargs['maximum'] = 25

        find = getattr(self.pd, entity).find(**kwargs): 
        found = []
        for f in find:
            found.append(f.json)

        #use pypd method entity.json to return the entity as json
        return found

    def delete(self, entity=None, _id=None, **kwargs):
        """ base delete() method defined in pypd.entity.delete() usable by most entities
        """
        if _id is None:
            raise InvalidArguments(_id)
        delete = getattr(self.pd, entity).delete(id=_id, **kwargs)
        if delete is True:
            return json.loads('{"deleted":true}')
        else:
            #use pypd method entity.json to return the entity as json
            return delete.json

    def create(self, entity=None, from_email=None, **kwargs):
        """ base create() method defined in pypd.entity.create() usable by most entities
        """
        if from_email is None:
            raise InvalidArguments(from_email)

        payload = json.dumps(kwargs)

        create = getattr(self.pd, entity).create(data=payload, from_email=from_email, **kwargs)
        #use pypd method entity.json to return the entity as json
        return create.json

    def send_payload(self, entity=None, method=None, _id=None, payload=None, **kwargs):
        """ base POST method to handle other POST type methods
            Make sure to use the PD API reference to determine if your action needs a `from` (use action parameter `from_email`)

            Payload should be a JSON string with the keys and values as defined from the PD API reference
            For some reason all the examples will have one extra top level key that should be omitted.
            For example, in Teams/put_teams_id the payload ('team') example is
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
        #check for required fields
        if not _id:
            raise InvalidArguments(_id)
        if not payload:
            raise InvalidArguments(payload)

        post = getattr(getattr(self.pd, entity), ("%s(id=%s, payload=%s, %s" % method, _id, payload, **kwargs))
        #use pypd method entity.json to return the entity as json
        return post.json

    put = post #if someone assumes they should use put(), its really the same logic as post()