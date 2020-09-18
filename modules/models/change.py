from datetime import datetime
from uuid import UUID

from pony.orm import Required, PrimaryKey

from .base import UniqueIdentifiedModel
from .document import Document


class Change(UniqueIdentifiedModel):
    _table_ = 'changes'
    id = PrimaryKey(UUID, auto=True)
    document = Required(Document)
    timestamp = Required(datetime)
    contents_diff = Required(bytes)
