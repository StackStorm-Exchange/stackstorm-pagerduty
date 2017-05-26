from lib.action import PagerDutyAction


class AckIncident(PagerDutyAction):
    def run(self, **param_dict):
        """
        Acknowledgment of a trigger. The PagerDuty v2 API requires that
        an incident be acknowledged using a valid email address. param_dict
        is a dictionary with key = incident_key, and value = email.
        """

        # TODO: Do we need to optionally be able to specify the service key?

        for incident_key, email in param_dict.iteritems():
            if email is None:
                raise ValueError("%s has empty email", incident_key)
            else:
                incident = self.pager.Incident.find_one(incident_key)
                incident.acknowledge(from_email=email)

        return param_dict.keys()
