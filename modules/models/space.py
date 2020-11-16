from uuid import UUID

from pony.orm import PrimaryKey, Required, Set

from modules.models.document import Document
from modules.models.folder import Folder
from modules.models.db import db
from modules.models.user import User


class Space(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    user = Required(User)
    documents = Set(Document)
    folders = Set(Folder)