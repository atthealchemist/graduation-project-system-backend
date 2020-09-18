from enum import Enum
from uuid import UUID

from pony.orm import Required, PrimaryKey

from modules.models import DB


class Role(Enum):
    ADMIN = 0
    READ_WRITE = 1
    READ_ONLY = 2


class User(DB.Entity):
    _table_ = 'users'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    password_hash = Required(str)
    salt = Required(str)
    login = Required(str, unique=True)
    token = Required(str, unique=True)
    role = Required(int, sql_default=str(Role.READ_ONLY.value))
