from launch_incident import LaunchIncident
from st2tests.base import BaseActionTestCase


class PagerDutyLaunchIncidentActionTestCase(BaseActionTestCase):
    action_cls = LaunchIncident
    full_config = {'api_key': 'abc1234', 'service_key': 'abc1234'}

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)
