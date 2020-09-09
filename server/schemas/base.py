from datetime import datetime
from uuid import UUID

from fastapi_utils.api_model import APIModel


class UniqueIdentifiedModel(APIModel):
    id: UUID


class TimestampedModel(APIModel):
    created_at: datetime
    updated_at: datetime


class NamedModel(UniqueIdentifiedModel):
    name: str


class TitledModel(NamedModel):
    title: str


class TitledDescriptedModel(TitledModel):
    description: str
