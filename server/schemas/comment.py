from typing import List
from uuid import UUID

from .base import UniqueIdentifiedModel
from .user import User


class Answer(UniqueIdentifiedModel):
    comment: UUID
    text: str


class Comment(UniqueIdentifiedModel):
    user: User
    text: str

    answers: List[Answer]


