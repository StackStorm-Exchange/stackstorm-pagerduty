from lib.action import PagerDutyAction


class LogEntriesIncident(PagerDutyAction):
    def run(self, time_zone, is_overview, include, fetch_all, ids):
        """
        Display log entries for an incident. ids is an array of incident ids.
        """

        for id in ids:
            query_params = {'id': id}
            incident = self.pager.Incident.fetch(limit=1, **query_params)
            entries = incident.log_entries(time_zone, is_overview, include, fetch_all)
            for entry in entries:
                print entry

        return ids
