from datetime import datetime
from typing import List, Optional
from uuid import UUID

from .base import UniqueIdentifiedSchema
from .user import UserSchema


class CommentSchema(UniqueIdentifiedSchema):
    user: UserSchema
    text: str
    created_at: datetime
    document_uuid: UUID

    answer_to: Optional[UUID]


