from enum import Enum

from pydantic import BaseModel

from .base import UniqueIdentifiedSchema


class Role(Enum):
    ADMIN = 0
    GUEST = 1
    USER = 2

    @staticmethod
    def is_admin(user):
        return user.role == Role.ADMIN

    @staticmethod
    def is_guest(user):
        return user.role == Role.GUEST

    @staticmethod
    def is_user(user):
        return user.role == Role.USER


class UserSchema(BaseModel):
    display_name: str
    password: str
    login: str

'''
{
  "display_name": "Hanyuu Furude",
  "password": "thatqtg1Rl)",
  "login": "hanyuu"
}
'''

class Admin(UserSchema):
    role = Role.ADMIN


class Reader(UserSchema):
    role = Role.READ_ONLY
