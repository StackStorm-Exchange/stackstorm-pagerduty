from lib.action import PagerDutyAction


class AckIncident(PagerDutyAction):
    def run(self, email, ids):
        """
        Acknowledgment of a trigger. The PagerDuty v2 API requires that
        an incident be acknowledged using a valid email address. ids is
        an array of incident ids.
        """

        # TODO: Do we need to optionally be able to specify the service key?

        if email is None:
            raise ValueError("email must be specified")

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.acknowledge(from_email=email)

        return ids
