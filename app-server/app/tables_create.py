from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from user import User

# debug purpose only
# from external.session_scope import session_scope

engine = create_engine('postgres://{}:{}@{}/{}'
                        .format(environ.get('DB_USER'),
                                environ.get('DB_PASSWORD'),
                                environ.get('DB_HOST'),
                                environ.get('DB_NAME')),
                        echo=True)
Base = declarative_base()
User.__table__.create(engine)

# with session_scope() as session:
#     user = User()
#     user.id = event['data']['id']
#     user.channel = event['data']['channel']
#     user.password = event['data']['password']
#     if 'worker' in event['data']['roles']:
#         user.is_worker = True
#     session.add(user)
#
# with session_scope() as session:
#     user = session.query(User).get(event2['issuer']['issuer']['id'])
#     user.avatar = event2['data']['avatar']
#     user.bio = event2['data']['bio']
#     user.email = event2['data']['email']
#     user.name = event2['data']['name']
#     session.add(user)
