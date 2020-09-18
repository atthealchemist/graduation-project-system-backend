from datetime import datetime
from uuid import UUID

from pony.orm import Required, PrimaryKey

from modules.models import DB


class UniqueIdentifiedModel(DB.Entity):
    _table_ = 'unique_identified_models'

    id = PrimaryKey(UUID, auto=True)


class TimestampedModel(DB.Entity):
    _table_ = 'timestamped_models'

    created_at = Required(datetime)
    updated_at = Required(datetime)


class NamedModel(DB.Entity):
    _table_ = 'named_models'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)


class TitledModel(DB.Entity):
    _table_ = 'titled_models'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    title = Required(str, 96)


class TitledDescriptedModel(DB.Entity):
    _table_ = 'titled_descripted_models'

    id = PrimaryKey(UUID, auto=True)
    name = Required(str, 32)
    title = Required(str, 96)
    description = Required(str)
