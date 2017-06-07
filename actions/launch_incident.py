from lib.action import PagerDutyAction


class LaunchIncident(PagerDutyAction):
    def run(self, description, event_type='trigger', incident_key=None, details=None):
        """Create a trigger"""

        payload = {
            'service_key': self.config['service_key'],
            'event_type': event_type,
            'description': description,
        }
        if details is not None:
            payload['details'] = details

        result = self.pager.Event.create(data=payload)

        return result
