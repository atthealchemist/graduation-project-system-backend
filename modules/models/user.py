from datetime import datetime
from uuid import UUID

from pony.orm import PrimaryKey, Optional, Set, Required

from modules.models.document import Document
from modules.models.db import db


class User(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    display_name = Optional(str)
    password_hash = Optional(str)
    password_salt = Optional(str)
    login = Optional(str, unique=True)
    token = Optional(str, unique=True)
    role = Optional(int, default=2)
    documents = Set(Document)
    comments = Set('Comment')
    changes = Set('Change')
    space = Optional('Space')
    acceses = Set('Access')
    created_at = Required(datetime, default=lambda: datetime.now())