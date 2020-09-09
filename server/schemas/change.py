from datetime import datetime

from .base import UniqueIdentifiedModel
from .document import Document


class Change(UniqueIdentifiedModel):
    document: Document
    timestamp: datetime
    contents_before: bytes
    contents_after: bytes
