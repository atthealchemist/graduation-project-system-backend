from enum import Enum
from typing import Optional
from uuid import UUID

from modules.schemas.base import UniqueIdentifiedSchema
from modules.schemas.user import UserSchema


class AccessType(Enum):
    READ_ONLY = 'ro'
    READ_WRITE = 'rw'
    ADMIN = 'rwx'


class AccessSchema(UniqueIdentifiedSchema):
    type: str
    document_uuid: Optional[UUID]
    user: Optional[UserSchema]
