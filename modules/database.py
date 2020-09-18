from pony.orm import db_session, commit, show

from modules.logger import ConsoleLogger
from modules.models.base import DB
from modules.utils import load_config


def init_database():
    db_config = load_config(section='database')
    mgr = DatabaseManager(
        db_object=DB,
        engine=db_config.get('engine'),
        host=db_config.get('host'),
        user=db_config.get('user'),
        password=db_config.get('password'),
        db_name=db_config.get('db_name')
    )
    return mgr


class DatabaseManager:

    @staticmethod
    def purge_db():
        with db_session:
            DB.drop_all_tables(with_all_data=True)

    def add(self, table, **params):
        logger = ConsoleLogger("DbManager::ADD")
        with db_session:
            for obj in table.select(lambda e: e.login == params.get('login')):
                if obj:
                    logger.error("Object {} already exists in database!".format(obj))
                    return
            obj = table(**params)
            commit()
            logger.debug("Created new {}".format(obj))

    def create(self, orm_obj, **params):
        self.add(orm_obj, **params)

    @staticmethod
    def delete(orm_obj):
        DatabaseManager.remove(orm_obj)

    @staticmethod
    def remove(table, uuid=''):
        logger = ConsoleLogger("DbManager::ADD")
        with db_session:
            if not uuid:
                logger.error('Are you kidding me? How can I drop user without identifier?')
                return
            removed_entity = table.select(lambda e: e.id == uuid)
            logger.debug("Removing {} from {}".format(removed_entity, table))
            removed_entity.delete()

    @staticmethod
    def update(table, uuid='', **params):
        logger = ConsoleLogger("DbManager::UPDATE")
        with db_session:
            updated_entity = table.select(lambda e: e.id == uuid)
            updated_entity.set(**params)
            logger.debug("Updating {} object {} with next params {}".format(table, updated_entity, params))
            commit()

    @staticmethod
    def edit(orm_obj, **params):
        DatabaseManager.update(orm_obj, **params)

    def configure_db(self, db_object):
        print("Configuring database")
        if not db_object:
            return
        print("Generate mapping: creating tables... ok!")
        db_object.generate_mapping(create_tables=True)

    def __init__(self, db_object, engine, host, user, password, db_name, logger=None):
        self.logger = logger
        if not db_object:
            return

        db_object.bind(
            provider=engine,
            user=user,
            password=password,
            host=host,
            database=db_name
        )
        print("Connecting to database {}@{}/{}... ok!".format(user, host, db_name))

        self.configure_db(db_object)


