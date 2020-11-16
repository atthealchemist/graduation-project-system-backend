from pony.orm import PrimaryKey, Required

from modules.models.document import Document
from modules.models.db import db
from modules.models.user import User


class Access(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    type = Required(str)
    document = Required(Document)