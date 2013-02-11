
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


