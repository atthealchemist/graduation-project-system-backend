from enum import Enum

from .main import main as main_router
from .user import user as user_router
from .document import document as document_router
from .migration import migration as migration_router
from .space import space as space_router
from .converter import converter as converter_router


class ResponseStatus(Enum):
    GOT = 'got'
    LISTED = 'listed'
    CREATED = 'created'
    UPDATED = 'updated'
    DELETED = 'deleted'
    ERROR = 'error'

    def __getattr__(self, item):
        return item.value

    def __getitem__(self, item):
        return item.value
