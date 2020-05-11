from os import environ
from sqlalchemy import create_engine
from pprint import pprint

engine = create_engine('postgres://{}:{}@{}/{}'
                        .format(environ.get('DB_USER'),
                                environ.get('DB_PASSWORD'),
                                environ.get('DB_HOST'),
                                environ.get('DB_NAME')),
                        echo=True)
pprint(engine.table_names())
