from uuid import UUID

from pony.orm import PrimaryKey, Required, Set

from modules.models.document import Document
from modules.models.db import db


class Link(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    name = Required(str)
    url = Required(str)
    documents = Set(Document)