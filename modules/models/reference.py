from datetime import datetime
from uuid import UUID

from pony.orm import PrimaryKey, Required

from modules.models.document import Document
from modules.models.db import db


class Reference(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    document = Required(Document)
    created_at = Required(datetime, default=lambda: datetime.now())