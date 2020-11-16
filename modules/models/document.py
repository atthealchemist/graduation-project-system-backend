from datetime import datetime
from uuid import UUID

from pony.orm import PrimaryKey, Required, Optional, Set
from pony.py23compat import buffer

from modules.models.db import db


class Document(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    title = Required(str, 96)
    created_at = Required(datetime, default=lambda: datetime.now())
    updated_at = Required(datetime, default=lambda: datetime.now())
    slug = Required(str)
    url = Optional(str)
    short_url = Optional(str)
    contents = Required(buffer)
    author = Required('User')
    comments = Set('Comment')
    changes = Set('Change')
    assets = Set('Asset')
    links = Set('Link')
    references = Set('Reference')
    folders = Set('Folder')
    spaces = Set('Space')
    acceses = Set('Access')