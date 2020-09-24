from datetime import datetime
from uuid import UUID

from .base import UniqueIdentifiedSchema


class ChangeSchema(UniqueIdentifiedSchema):
    document_uuid: UUID
    timestamp: datetime
    contents_before: bytes
    contents_after: bytes
