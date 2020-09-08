
from uuid import UUID

from fastapi_utils.api_model import APIModel


class UniqueIdentifiedModel(APIModel):
    uuid: UUID


class NamedModel(UniqueIdentifiedModel):
    uuid: UUID
    name: str


class TitledModel(NamedModel):
    title: str


class TitledDescriptedModel(TitledModel):
    description: str
