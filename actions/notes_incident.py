from lib.action import PagerDutyAction


class notesIncident(PagerDutyAction):
    def run(self, ids):
        """
        Display notes for an incident. ids is an array of incident ids.
        """

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            print incident.notes()

        return ids
