from datetime import datetime
from uuid import UUID

from pony.orm import PrimaryKey, Required

from modules.models.document import Document
from modules.models.db import db
from modules.models.user import User


class Change(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    changed_at = Required(datetime)
    user = Required(User)
    content_diff = Required(str)
    document = Required(Document)