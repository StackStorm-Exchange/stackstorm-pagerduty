from lib.action import PagerDutyAction


class SnoozeIncident(PagerDutyAction):
    def run(self, duration, ids, from_email):
        """
        Snooze incident for specified amount of time. ids is an array of
        incident ids.
        """

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.snooze(from_email, duration)

        return ids
