from uuid import UUID

from pony.orm import Required, PrimaryKey

from modules.models import DB


class Asset(DB.Entity):
    _table_ = 'assets'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    contents = Required(bytes)
