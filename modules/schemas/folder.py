from typing import List

from .base import NamedSchema, UniqueIdentifiedSchema
from .document import DocumentSchema


class FolderSchema(UniqueIdentifiedSchema):
    display_name: str
    documents: List[DocumentSchema]

    folders: List[FolderSchema]
