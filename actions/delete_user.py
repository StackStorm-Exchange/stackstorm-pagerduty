from lib.action import PagerDutyAction
from pypd.errors import BadRequest


class DeleteUser(PagerDutyAction):
    def run(self, email):
        """
        Delete a user from PagerDuty (`or raise an error if not possible)

        :param email: The
        :return: (success (bool), results (obj).
        """
        success = True
        results = {
            "user_id": None,
            "error": None
        }

        users = self.pager.User.find(email=email)

        if users:
            if len(users) == 1:
                results['user_id'] = users[0].id
                try:
                    users[0].remove()
                except BadRequest as e:
                    success = False
                    results['error'] = str(e)
            else:
                results['error'] = "Found {} users!".format(len(users))
                success = False
        else:
            results['error'] = "Found {} users!".format(len(users))
            success = False

        return success, results
