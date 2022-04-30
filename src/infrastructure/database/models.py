from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()


# an example mapping using the base
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
