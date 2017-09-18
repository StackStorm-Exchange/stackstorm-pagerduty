from lib.action import PagerDutyAction
from pypd.errors import BadRequest


class LaunchIncident(PagerDutyAction):
    def run(self, title, from_email=None, incident_key=None, details=None):
        """Create a trigger"""

        escalation_policy = self.pager.EscalationPolicy.find_one()
        service = self.pager.Service.find_one()

        payload = {
            'type': 'incident',
            'title': title,
            'service': {
                'id': service['id'],
                'type': 'service_reference',
            },
            'incident_key': incident_key,
            'escalation_policy': {
                'id': escalation_policy['id'],
                'type': 'escalation_policy_reference',
            }
        }

        if details is not None:
            payload['body'] = {
                'details': details,
                'type': 'incident_body',
            }

        try:
            incident = self.pager.Incident.create(
                data=payload,
                add_headers={'from': from_email, },
            )
        except BadRequest as e:
            print(e)

        return incident
