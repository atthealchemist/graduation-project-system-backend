from uuid import UUID

from pony.orm import db_session, commit
from pony.orm.serialization import to_dict

from modules.logger import ConsoleLogger
from modules.models.generated import db as DB
from modules.utils import load_config

logger = ConsoleLogger("DatabaseManager")


def init_database():
    db_config = load_config(section='database')

    DB.bind(
        provider=db_config.get('engine'),
        user=db_config.get('user'),
        password=db_config.get('password'),
        host=db_config.get('host'),
        database=db_config.get('db_name')
    )
    logger.debug("Connecting to database {}@{}/{}... ok!".format(
        db_config.get('user'),
        db_config.get('host'),
        db_config.get('db_name')
    ))

    logger.debug("Configuring database")
    if not DB:
        logger.error("Error: database is not initialized or created!")
        return
    DB.generate_mapping(create_tables=True)
    logger.debug("Generate mapping: creating tables... ok!")


class DatabaseManager:

    @staticmethod
    def find(table, query):
        return DatabaseManager.get(table, query)

    @staticmethod
    def all(table):
        with db_session:
            entities = table.select()
            return [to_dict(e) for e in entities]

    @staticmethod
    def get(table, query, as_entity=False):
        with db_session:
            entities_list = list(filter(query, table.select()))
            if len(entities_list) == 1:
                entities_list = entities_list[0]
            result = to_dict(entities_list)
            if as_entity:
                result = entities_list
        return result

    @staticmethod
    def purge_db():
        with db_session:
            DB.drop_all_tables(with_all_data=True)

    @staticmethod
    def add(table, **params):
        DatabaseManager.create(table, **params)

    @staticmethod
    def create(table, **params):
        with db_session:
            obj = table(**params)
            commit()
            logger.debug("Created new {}".format(obj))
            return obj

    @staticmethod
    def delete(table, uuid):
        DatabaseManager.remove(table, uuid)

    @staticmethod
    def remove(table, uuid=''):
        with db_session:
            removed_entity = list(filter(lambda e: e.id == UUID(uuid), table.select()))[0]
            logger.debug("Removing {} from {}".format(removed_entity, table.__name__))
            removed_entity.delete()

    @staticmethod
    def update(table, uuid='', **params):
        with db_session:
            updated_entity = list(filter(lambda e: e.id == UUID(uuid), table.select()))[0]
            updated_entity.set(**params)
            logger.debug("Updating {} object {} with next params {}".format(table.__name__, updated_entity, params))
            commit()
            return updated_entity

    @staticmethod
    def edit(orm_obj, **params):
        DatabaseManager.update(orm_obj, **params)
