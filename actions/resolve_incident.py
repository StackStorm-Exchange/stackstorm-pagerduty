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
            raise ValueError("email must be specified")

        for key in keys:
            query_params = {'id': key}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.resolve(from_email=email)

        return keys
