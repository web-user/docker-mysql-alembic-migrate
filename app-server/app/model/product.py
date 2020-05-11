from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(256), default=None)
    last_name = Column(String(256), default=None)

class Shmuser(Base):
    __tablename__ = 'shmuser'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(256), default=None)
    last_name = Column(String(256), default=None)
    test_data = Column(String(256), default=None)