from modules.database import init_database
from modules.models.user import User
from modules.utils import generate_jwt_token, encrypt_password, random_string, encrypt_base64


def test_database_manager():
    mgr = init_database()

    mgr.create(
        User,
        name="Hanyuu Furude",
        login=encrypt_base64(''.join(reversed("bokuwahanyuu"))),
        password_hash=encrypt_password("hellomynameishanyuu:)"),
        salt=random_string(64),
        token=generate_jwt_token()
    )


if __name__ == '__main__':
    test_database_manager()
