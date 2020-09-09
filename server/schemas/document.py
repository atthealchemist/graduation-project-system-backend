from typing import List

from .asset import Asset
from .base import TitledModel, TimestampedModel
from .change import Change
from .comment import Comment
from .link import Link


class Document(TitledModel, TimestampedModel):
    slug: str
    url: str
    short_url: str
    contents: bytes

    references: List[str]
    links: List[Link]
    assets: List[Asset]

    changes: List[Change]
    comments: List[Comment]
