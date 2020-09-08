from typing import List

from .base import NamedModel
from .document import Document


class BaseFolder(NamedModel):
    documents: List[Document]


class Folder(BaseFolder):
    subfolders: List[BaseFolder]
