from typing import List

from .asset import Asset
from .base import TitledSchema, TimestampedSchema
from .change import Change
from .comment import Comment
from .link import Link


class Document(TitledSchema, TimestampedSchema):
    slug: str
    url: str
    short_url: str
    contents: str

    references: List[str]
    links: List[Link]
    assets: List[Asset]

    changes: List[Change]
    comments: List[Comment]
