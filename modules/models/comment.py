from uuid import UUID

from pony.orm import Set, Required, PrimaryKey

from modules.models import DB
from modules.models.user import User


class Comment(DB.Entity):
    _table_ = 'comments'

    id = PrimaryKey(UUID, auto=True)
    user = Required(User)
    text = Required(str)
    answers = Set('Comment')

