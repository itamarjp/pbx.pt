
from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    DateTime,
    Date,
    Boolean,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

#class User(object):
#    def __init__(self, login, password, groups=None):
#        self.login = login
#        self.password = password
#        self.groups = groups or []
#
#    def check_password(self, passwd):
#        return self.password == passwd

class Group(Base):
    __tablename__ = 'group'
    group_id = Column(Integer, autoincrement=True, primary_key=True)
    group_name = Column(Unicode(16), unique=True)
    display_name = Column(Unicode(255))
    created = Column(DateTime)


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    email_address = Column(Unicode(255), unique=True)
    display_name = Column(Unicode(255))
    password = Column(Unicode(40))
    created = Column(DateTime)

    @classmethod
    def by_email(cls, email):
      return DBSession.query(User).filter(User.email_address == email).first()

    def verify_password(self, password):
      return self.password == password


class Extension(Base):
    __tablename__ = 'ramais'
    extension_id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(Unicode(40))
    user_id = Column(Integer)
    active = Column(Boolean)


