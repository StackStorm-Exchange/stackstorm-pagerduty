from lib.action import PagerDutyAction


class LaunchIncident(PagerDutyAction):
    def run(self, description, event_type='trigger', details=None):
        """Create a trigger"""

        result = self.pager.Event.create(data={
            'service_key': self.config['service_key'],
            'event_type': event_type,
            'description': description,
            'details': details
        })

        return result
