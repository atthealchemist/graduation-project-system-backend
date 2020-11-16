from datetime import datetime
from uuid import UUID

from pony.orm import PrimaryKey, Required

from modules.models.document import Document
from modules.models.db import db
from modules.models.user import User


class Comment(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    text = Required(str)
    created_at = Required(datetime)
    document = Required(Document)
    user = Required(User)