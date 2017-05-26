from lib.action import PagerDutyAction


class ResolveIncident(PagerDutyAction):
    def run(self, email, keys):
        """
        Resolve an incident. The PagerDuty v2 API requires that an incident
        be resolved using a valid email address. keys is an array of
        incident keys.
        """

        # TODO: Do we need to be able to optionally specify the service key?

        if email is None:
            raise ValueError("email must be specified", email)

        for key in keys:
            incident = self.pager.Incident.find_one(key)
            incident.resolve(from_email=email)

        return keys
