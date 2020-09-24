from enum import Enum

from pydantic import BaseModel

from .base import UniqueIdentifiedSchema


class Role(Enum):
    ADMIN = 0
    READ_WRITE = 1
    READ_ONLY = 2


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
