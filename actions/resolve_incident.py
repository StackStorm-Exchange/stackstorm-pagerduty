from lib.action import PagerDutyAction


class ResolveIncident(PagerDutyAction):
    def run(self, from_email, resolution, ids):
        """
        Resolve an incident. The PagerDuty v2 API requires that an incident
        be resolved using a valid email address. ids is an array of
        incident ids.
        """

        if from_email is None:
            raise ValueError("from_email must be specified")

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.resolve(from_email, resolution)

        return ids
