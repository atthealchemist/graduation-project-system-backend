from .base import UniqueIdentifiedModel
from .document import Document


class Reference(UniqueIdentifiedModel):
    document: Document
