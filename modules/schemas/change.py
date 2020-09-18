from datetime import datetime

from .base import UniqueIdentifiedSchema
from .document import Document


class Change(UniqueIdentifiedSchema):
    document: Document
    timestamp: datetime
    contents_before: bytes
    contents_after: bytes
