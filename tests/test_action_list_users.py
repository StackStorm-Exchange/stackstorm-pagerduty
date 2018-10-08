from mock import MagicMock

from list_users import ListUsers
from st2tests.base import BaseActionTestCase


class PagerDuytyListUsersActionTestCase(BaseActionTestCase):
    action_cls = ListUsers
    full_config = {'api_key': 'abc1234', 'service_key': 'abc1234'}

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)

    def test_run_user_list(self):
        expected = [
            {'id': 'PD1234', 'email': 'bob@example.com'},
            {'id': 'PD5678', 'email': 'fred@example.com'},
        ]

        action = self.get_action_instance(self.full_config)
        action.pager.User.find = MagicMock(return_value=[{'id': 'PD1234', 'email': 'bob@example.com'},
                                                         {'id': 'PD5678', 'email': 'fred@example.com'}
                                                         ]
                                           )

        result = action.run()
        self.assertEqual(result, expected)
