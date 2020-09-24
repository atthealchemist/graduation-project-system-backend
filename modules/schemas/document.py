from typing import List, Optional, ForwardRef

from .asset import AssetSchema
from .base import TitledSchema, TimestampedSchema
from .user import UserSchema

# !!! DO NOT REMOVE THOSE UNUSED SCHEMAS, THEY'RE USED BY FORWARD REF !!! #

from .reference import ReferenceSchema
from .link import LinkSchema
from .access import AccessSchema
from .change import ChangeSchema
from .comment import CommentSchema
from .access import AccessSchema


class DocumentSchema(TitledSchema, TimestampedSchema):
    slug: Optional[str]
    url: Optional[str]
    short_url: Optional[str]
    contents: Optional[str]

    author: UserSchema

    references: Optional[List[ReferenceSchema]]
    links: Optional[List[LinkSchema]]
    assets: Optional[List[AssetSchema]]

    changes: Optional[List[ChangeSchema]]
    comments: Optional[List[CommentSchema]]
    accesses: Optional[List[AccessSchema]]

