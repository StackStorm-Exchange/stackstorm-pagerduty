from lib.action import PagerDutyAction


class CreateUser(PagerDutyAction):
    def run(self, name, email, role, job_title, color="green"):
        """
        Create a user in PagerDuty.
        """

        user_data = {
            'type': 'user',
            'name': name,
            'email': email,
            'color': color,
            'role': role,
            'job_title': job_title,
            'description': name,
        }

        pd_user = self.pager.User.create(data=user_data,
                                         from_email=email)

        return pd_user.json
