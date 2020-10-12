from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pony.orm.serialization import to_dict

from modules.models.managers.user import UserManager
from modules.utils import extract_entity

auth_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login",
    scopes=dict(
        user="User scope",
        admin="Admin scope"
    )
)


def logged_in_as_user(token=Depends(auth_scheme)):
    user = UserManager.get_by_token(user_token=token)
    return extract_entity(to_dict(user), exclude_fields=('password_hash', 'password_salt', 'role'))


def logged_in_as_admin(token=Depends(auth_scheme)):
    user = UserManager.get_by_token(user_token=token)
    return extract_entity(to_dict(user), exclude_fields=('password_hash', 'password_salt'))
