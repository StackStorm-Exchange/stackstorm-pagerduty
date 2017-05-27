import pypd

from st2actions.runners.pythonrunner import Action


class PagerDutyAction(Action):
    def __init__(self, config):
        """ init method, run at class creation """
        super(PagerDutyAction, self).__init__(config)
        self.pager = self._init_client()
        self.trigger = []

    def _init_client(self):
        """ init_client method, run at class creation """
        pypd.api_key = self.config['api_key']
        pypd.service_key = self.config['service_key']
        return pypd

    def get_ack_incidents(self):
        """ Get all the acknowledged incidents """
        ack_alarms = []
        for incident in self.pager.Incident.find(statuses=['acknowledged']):
            ack_alarms.append(incident.incident_key)
        return ack_alarms

    def get_triggered_incidents(self):
        """ Get all the triggered incidents """
        trigger_alarms = []
        for incident in self.pager.Incident.find(statuses=['triggered']):
            trigger_alarms.append(incident.incident_key)
        return trigger_alarms
