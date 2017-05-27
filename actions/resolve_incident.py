from lib.action import PagerDutyAction


class ResolveIncident(PagerDutyAction):
    def run(self, email, ids):
        """
        Resolve an incident. The PagerDuty v2 API requires that an incident
        be resolved using a valid email address. ids is an array of
        incident ids.
        """

        # TODO: Do we need to be able to optionally specify the service key?

        if email is None:
            raise ValueError("email must be specified")

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.resolve(from_email=email)

        return ids
