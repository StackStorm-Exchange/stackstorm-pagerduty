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
        if entity is None:
            raise InvalidArguments(entity)
        if _id is None:
            raise InvalidArguments(_id)
        fetch = getattr(self.pd, entity).fetch(id=_id, **kwargs)
        #use pypd method entity.json to return the entity as json
        return fetch.json


    def find(self, entity=None, **kwargs):
        """ base find() method defined in pypd.entity.find() usable by all entities
        """
        if entity is None:
            raise InvalidArguments(entity)
        if not 'maximum' in kwargs:
            #if maximum was ommited from the action, or didn't have a default, make sure we don't have a rediculous response
            kwargs['maximum'] = 10

        find = getattr(self.pd, entity).find(**kwargs): 
        found = []
        for f in find:
            found.append(f.json)

        #use pypd method entity.json to return the entity as json
        return found


    def create(self, entity=None, from_email=None, **kwargs):
        """ base create() method defined in pypd.entity.create() usable by most entities
        """
        if entity is None:
            raise InvalidArguments(entity)
        if from_email is None:
            raise InvalidArguments(from_email)
        payload = {}
        for k, v in kwargs.iteritems():
            payload[k] = v
        create = getattr(self.pd, entity).create(data=json.dumps(payload), from_email=from_email)
        #use pypd method entity.json to return the entity as json
        return create.json


    def delete(self, entity=None, _id=None, **kwargs):
        """ base delete() method defined in pypd.entity.delete() usable by most entities
        """
        if entity is None:
            raise InvalidArguments(entity)
        if _id is None:
            raise InvalidArguments(_id)
        delete = getattr(self.pd, entity).delete(id=_id, **kwargs)
        if delete is True:
            return json.loads('{"deleted":true}')
        else:
            #use pypd method entity.json to return the entity as json
            return delete.json

    def other(self, entity=None, method=None, **kwargs):
        """ method for variable entity operations
        """ 
        if entity is None:
            raise InvalidArguments(entity)    
        if method is None:
            raise InvalidArguments(method)
        data = {}
        if kwargs.get('resource_id', None):
            resource_id = str(kwargs.pop('resource_id'))
            #if resource_id is present it means that we need to run the method against an existing resource, look it up
            resource = getattr(self.pd, entity).fetch(id=resource_id)

        if kwargs.get('from_email', None):
            from_email = str(kwargs.pop('from_email'))
            data['from_email'] = from_email

        payload = {}
        for k, v in kwargs.iteritems():
            payload[k] = v  
        data['data'] = json.dumps(payload) #assign payload as a string value to a key
        parameters = ''.join('{0}{1}'.format(key, val) for key, val in data.iteritems()) 

        if resource_id:

            result = setattr(resource, method, )


# class Error(Exception):
#     pass


# class MissingArguments(Error):
#     """ arguments that are required were missing or None
#     """
#     def __init__(self, *args):
