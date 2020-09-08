from typing import List

from .base import NamedModel
from .document import Document


class BaseFolder(NamedModel):
    folder_documents: List[Document]


class Folder(BaseFolder):
    folder_subfolders: List[BaseFolder]
