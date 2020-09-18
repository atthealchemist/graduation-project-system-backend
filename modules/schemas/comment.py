from typing import List
from uuid import UUID

from .base import UniqueIdentifiedSchema
from .user import User


class Answer(UniqueIdentifiedSchema):
    comment: UUID
    text: str


class Comment(UniqueIdentifiedSchema):
    user: User
    text: str

    answers: List[Answer]


