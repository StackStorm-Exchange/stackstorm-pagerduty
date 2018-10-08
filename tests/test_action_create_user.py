from create_user import CreateUser
from st2tests.base import BaseActionTestCase


class PagerDuytyCreateUserActionTestCase(BaseActionTestCase):
    action_cls = CreateUser

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)
