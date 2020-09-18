from enum import Enum

from .base import NamedSchema


class Role(Enum):
    ADMIN = 0
    READ_WRITE = 1
    READ_ONLY = 2


class User(NamedSchema):
    password_hash: str
    login: str
    token: str
    role: Role = Role.READ_WRITE


class Admin(User):
    role = Role.ADMIN


class Reader(User):
    role = Role.READ_ONLY
