from pony.orm.serialization import to_dict

from modules.database import DatabaseManager
from modules.models.generated import User
from modules.utils import encrypt_password, generate_jwt_token, extract_entity


class UserManager:

    @staticmethod
    def create_if_not_exists(login, password, display_name):
        created = False
        user = UserManager.get_by_login(login)
        if not user:
            password_hash, password_salt = encrypt_password(password)

            DatabaseManager.add(
                User,
                display_name=display_name,
                login=login,
                password_hash=password_hash,
                password_salt=password_salt,
                token=generate_jwt_token()
            )

            created = True

        return created

    @staticmethod
    def get_by_login(user_login):
        user = DatabaseManager.get(User, lambda u: u.login == user_login, as_entity=True)
        # user_extracted = extract_entity(user)
        return user

    @staticmethod
    def get_by_token(user_token):
        user = DatabaseManager.get(User, lambda u: u.token == user_token, as_entity=True)
        return user

    @staticmethod
    def as_dict(user, exclude_fields=()):
        return extract_entity(to_dict(user), exclude_fields=exclude_fields)
