from pony.orm import db_session, commit

from modules.logger import ConsoleLogger
from modules.models.base import DB
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
    logger.debug("Generate mapping: creating tables... ok!")
    DB.generate_mapping(create_tables=True)


class DatabaseManager:

    @staticmethod
    def find(table, query):
        return DatabaseManager.get(table, query)

    @staticmethod
    def all(table):
        with db_session:
            entities = table.select()
            return [e for e in entities]

    @staticmethod
    def get(table, query):
        with db_session:
            entities_list = [entity for entity in table.select(query)]
            if len(entities_list) == 1:
                entities_list = entities_list[0]
            return entities_list

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
            for obj in table.select(lambda e: e.login == params.get('login')):
                if obj:
                    logger.error("Object {} already exists in database!".format(obj))
                    return
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
            if not uuid:
                logger.error('Are you kidding me? How can I drop user without identifier?')
                return
            removed_entity = table.select(lambda e: e.id == uuid)
            logger.debug("Removing {} from {}".format(removed_entity, table))
            removed_entity.delete()

    @staticmethod
    def update(table, uuid='', **params):
        with db_session:
            updated_entity = table.select(lambda e: e.id == uuid)
            updated_entity.set(**params)
            logger.debug("Updating {} object {} with next params {}".format(table, updated_entity, params))
            commit()
            return updated_entity

    @staticmethod
    def edit(orm_obj, **params):
        DatabaseManager.update(orm_obj, **params)
