from lib.action import PagerDutyAction


class AckIncident(PagerDutyAction):
    def run(self, from_email, ids):
        """
        Acknowledgment of a trigger. The PagerDuty v2 API requires that
        an incident be acknowledged using a valid email address. ids is
        an array of incident ids.
        """

        if from_email is None:
            raise ValueError("email must be specified")

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.acknowledge(from_email)

        return ids
