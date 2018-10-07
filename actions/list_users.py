from lib.action import PagerDutyAction


class ListUsers(PagerDutyAction):
    def run(self, query=None):
        """
        Get the list of all users from PagerDuty.
        """
        users = []

        pd_users = self.pager.User.find()

        for pd_user in pd_users:
            users.append({
                "id": pd_user.id,
                "email": pd_user.email,
            })

        return users
