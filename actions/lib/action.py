import pypd

from st2actions.runners.pythonrunner import Action


class PagerDutyAction(Action):
    def __init__(self, config):
        super(PagerDutyAction, self).__init__(config)
        self.pager = self._init_client()
        self.trigger = []

    def _init_client(self):
        # TODO: Return pager object
        pypd.api_key = self.config['api_key']
        return pypd

    #  get all the acknowledged incidents
    def get_ack_incidents(self):
        ack_alarms = []
        for incident in self.pager.incidents.list(status="acknowledged"):
            ack_alarms.append(incident.incident_key)
        return ack_alarms

    #  get all the triggered incidents
    def get_triggered_incidents(self):
        trigger_alarms = []
        for incident in self.pager.incidents.list(status="triggered"):
            trigger_alarms.append(incident.incident_key)
        return trigger_alarms
