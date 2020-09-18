from typing import List

from .base import NamedSchema
from .document import Document


class BaseFolder(NamedSchema):
    documents: List[Document]


class Folder(BaseFolder):
    folders: List[BaseFolder]
    documents: List[Document]
