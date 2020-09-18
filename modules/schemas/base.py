from datetime import datetime
from uuid import UUID

from fastapi_utils.api_model import APIModel as APISchema


class UniqueIdentifiedSchema(APISchema):
    id: UUID


class TimestampedSchema(APISchema):
    created_at: datetime
    updated_at: datetime


class NamedSchema(UniqueIdentifiedSchema):
    name: str


class TitledSchema(NamedSchema):
    title: str


class TitledDescriptedSchema(TitledSchema):
    description: str
