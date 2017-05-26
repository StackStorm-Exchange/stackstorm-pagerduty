from lib.action import PagerDutyAction


class AckIncident(PagerDutyAction):
    def run(self, email, keys):
        """
        Acknowledgment of a trigger. The PagerDuty v2 API requires that
        an incident be acknowledged using a valid email address. keys is
        an array of incident keys.
        """

        # TODO: Do we need to optionally be able to specify the service key?

        if email is None:
            raise ValueError("email must be specified")

        for key in keys:
            incident = self.pager.Incident.find_one(key)
            incident.acknowledge(from_email=email)

        return keys
