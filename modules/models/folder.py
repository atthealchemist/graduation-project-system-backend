from uuid import UUID

from pony.orm import PrimaryKey, Optional, Set

from modules.models.document import Document
from modules.models.db import db


class Folder(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    display_name = Optional(str)
    documents = Set(Document)
    parent_folders = Set('Folder', reverse='child_folders')
    child_folders = Set('Folder', reverse='parent_folders')
    spaces = Set('Space')