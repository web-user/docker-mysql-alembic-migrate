from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from user import User


engine = create_engine('postgres://{}:{}@{}/{}'
                        .format(environ.get('DB_USER'),
                                environ.get('DB_PASSWORD'),
                                environ.get('DB_HOST'),
                                environ.get('DB_NAME')),
                        echo=True)
Base = declarative_base()
User.__table__.drop(engine)
