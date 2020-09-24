from typing import List, Optional

from modules.schemas.base import UniqueIdentifiedSchema
from modules.schemas.document import DocumentSchema
from modules.schemas.folder import FolderSchema
from modules.schemas.user import UserSchema


class Space(UniqueIdentifiedSchema):
    user: UserSchema
    documents: Optional[List[DocumentSchema]]
    folders: Optional[List[FolderSchema]]
