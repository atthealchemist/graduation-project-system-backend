from datetime import datetime
from uuid import UUID

from pony.orm.core import Required, Set, PrimaryKey

from modules.models import DB


class Document(DB.Entity):
    _table_ = 'documents'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    title = Required(str, 96)

    created_at = Required(datetime)
    updated_at = Required(datetime)

    slug = Required(str)
    url = Required(str)
    short_url = Required(str)
    contents = Required(bytes)

    references = Set('Reference')
    links = Set('Link')
    assets = Set('Asset')

    changes = Set('Change')
    comments = Set('Comment')

