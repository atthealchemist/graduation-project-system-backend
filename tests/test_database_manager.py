import unittest

from modules.core.database import init_database
from modules.core.utils import encrypt_base64, encrypt_password, random_string, generate_jwt_token
from modules.models.user import User


class DatabaseManagerTestCase(unittest.TestCase):
    def test_database_manager_create_new_user(self):
        mgr = init_database()

        user = mgr.create(
            User,
            name="Hanyuu Furude",
            login=encrypt_base64(''.join(reversed("bokuwahanyuu"))),
            password_hash=encrypt_password("hellomynameishanyuu:)"),
            salt=random_string(64),
            token=generate_jwt_token()
        )
        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
