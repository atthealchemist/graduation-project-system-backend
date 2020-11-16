from uuid import UUID

from pony.orm import PrimaryKey, Required, Set, Optional
from pony.py23compat import buffer

from modules.models.document import Document
from modules.models.db import db


class Asset(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str)
    content = Required(buffer)
    documents = Set(Document)
    mime_type = Optional(str)