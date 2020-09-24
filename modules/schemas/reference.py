from uuid import UUID

from .base import UniqueIdentifiedSchema


class ReferenceSchema(UniqueIdentifiedSchema):
    document_uuid: UUID
