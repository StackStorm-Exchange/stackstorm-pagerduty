from mock import MagicMock

from list_users import ListUsers
from st2tests.base import BaseActionTestCase


class PdUser(object):
    def __init__(self, pd_id, email):
        self._pd_id = pd_id
        self._email = email

    @property
    def id(self):
        return self._pd_id

    @property
    def email(self):
        return self._email


class PagerDuytyListUsersActionTestCase(BaseActionTestCase):
    action_cls = ListUsers
    full_config = {'api_key': 'abc1234', 'service_key': 'abc1234'}

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)

    def test_run_list_user_empty(self):
        expected = []

        action = self.get_action_instance(self.full_config)
        action.pager.User.find = MagicMock(
            return_value=[]
        )

        result = action.run()
        self.assertEqual(result, expected)

    def test_run_list_user_single(self):
        expected = [
            {'id': 'PD1234', 'email': 'bob@example.com'},
            {'id': 'PD5678', 'email': 'fred@example.com'},
        ]

        action = self.get_action_instance(self.full_config)
        action.pager.User.find = MagicMock(
            return_value=[PdUser('PD1234', 'bob@example.com')]
        )

        result = action.run()
        self.assertEqual(result, expected)

    def test_run_list_user_multiple(self):
        expected = [
            {'id': 'PD1234', 'email': 'bob@example.com'},
            {'id': 'PD5678', 'email': 'fred@example.com'},
        ]

        action = self.get_action_instance(self.full_config)
        action.pager.User.find = MagicMock(
            return_value=[PdUser('PD1234', 'bob@example.com'),
                          PdUser('PD5678', 'fred@example.com')]
        )

        result = action.run()
        self.assertEqual(result, expected)
