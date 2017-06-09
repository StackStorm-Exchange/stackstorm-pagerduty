from lib.action import PagerDutyAction


class CreateNoteIncident(PagerDutyAction):
    def run(self, content, from_email, ids):
        """
        Create note attached to an incident. ids is an array of incident ids.
        """

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            incident.create_note(from_email, content)

        return ids
