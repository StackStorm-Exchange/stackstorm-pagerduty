from mock import MagicMock

from delete_user import DeleteUser
from st2tests.base import BaseActionTestCase


class PdUser(object):
    @property
    def id(self):
        return 'PD1234'

    @property
    def email(self):
        return 'bob@example.com'

    @staticmethod
    def remove():
        return True


class BadRequest(object):
    pass


class PagerDuytyDeleteUserActionTestCase(BaseActionTestCase):
    action_cls = DeleteUser
    full_config = {'api_key': 'abc1234', 'service_key': 'abc1234'}

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)

    def test_run_removal_success(self):
        expected = {"user_id": "PD1234", "error": None}

        action = self.get_action_instance(self.full_config)

        action.pager.User.find = MagicMock(
            return_value=[PdUser()]
        )

        (success, result) = action.run()
        self.assertTrue(success)
        self.assertEqual(result, expected)

    def test_run_no_users(self):
        expected = {"user_id": None, "error": "Found 0 users!"}

        action = self.get_action_instance(self.full_config)

        action.pager.User.find = MagicMock(return_value=[])

        (success, result) = action.run()
        self.assertFalse(success)
        self.assertEqual(result, expected)
