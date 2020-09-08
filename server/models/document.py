from typing import List

from .asset import Asset
from .base import TitledModel
from .change import Change
from .link import Link


class Document(TitledModel):
    slug: str
    url: str
    short_url: str
    contents: bytes

    references: List[str]
    links: List[Link]
    assets: List[Asset]

    changes: List[Change]
