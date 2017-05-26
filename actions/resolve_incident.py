from lib.action import PagerDutyAction


class ResolveIncident(PagerDutyAction):
    def run(self, **param_dict):
        """
        Resolve an incident. The PagerDuty v2 API requires that an incident
        be resolved using a valid email address. param_dict is a dictionary
        with key = incident_key, and value = email.
        """

        # TODO: Do we need to be able to optionally specify the service key?

        for incident_key, email in param_dict.iteritems():
            if email is None:
                raise ValueError("%s has empty email", incident_key)
            else:
                incident = self.pager.Incident.find_one(incident_key)
                incident.resolve(from_email=email)

        return param_dict.keys()
