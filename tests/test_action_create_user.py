from mock import MagicMock

from create_user import CreateUser
from st2tests.base import BaseActionTestCase


class PdUser(object):
    @property
    def id(self):
        return 'PD1234'

    @property
    def email(self):
        return 'bob@example.com'

    @property
    def json(self):
        return {"id": self.id, "email": self.email}


class PagerDuytyCreateUserActionTestCase(BaseActionTestCase):
    action_cls = CreateUser
    full_config = {'api_key': 'abc1234', 'service_key': 'abc1234'}

    def test_run_is_instance(self):
        action = self.get_action_instance(self.full_config)
        self.assertIsInstance(action, self.action_cls)

    def test_run_create_success(self):
        expected = {"user_id": "PD1234", "email": 'bob@example.com'}

        action = self.get_action_instance(self.full_config)

        action.pager.User.create = MagicMock(
            return_value=PdUser()
        )

        (success, result) = action.run(
            name="Bob",
            email='bob@example.com',
            role="user",
            job_title="Chef cook and bottle washer"
        )
        self.assertTrue(success)
        self.assertEqual(result, expected)
