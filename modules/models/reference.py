from uuid import UUID

from pony.orm import Set, PrimaryKey

from modules.models import DB


class Reference(DB.Entity):
    _table_ = 'references'

    id = PrimaryKey(UUID, auto=True)
    document = Set('Document')
