from uuid import UUID

from pony.orm import Required, PrimaryKey

from modules.models import DB


class Link(DB.Entity):
    _table_ = 'links'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    url = Required(str)
