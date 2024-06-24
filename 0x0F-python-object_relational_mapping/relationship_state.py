#!/usr/bin/python3

"""this module is for connecting to mysql database
by using sqlalchemy module"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sys
Base = declarative_base()


class State(Base):
    """State class inherentend from Base and he's
    representing the database structure"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')


if __name__ == '__main__':
    args = sys.argv[1:]
    passwrd = args[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
