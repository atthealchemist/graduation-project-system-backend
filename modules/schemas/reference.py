from .base import UniqueIdentifiedSchema
from .document import Document


class Reference(UniqueIdentifiedSchema):
    document: Document
