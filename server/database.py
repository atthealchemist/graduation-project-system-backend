import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from server.utils import load_config

config = load_config()
db_config = config['database']

DATABASE_URL = "{db_engine}://{db_user}:{db_passwd}@{db_url}/{db_scheme}".format(
    db_engine=db_config['engine'],
    db_url=db_config['url'],
    db_user=db_config['user'],
    db_passwd=db_config['password'],
    db_scheme=db_config['scheme']
)

engine = sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



