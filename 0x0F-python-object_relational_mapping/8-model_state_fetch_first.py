#!/usr/bin/python3
"""this module is for connecting to mysql database
    and fetching all data from state table
    by using sqlalchemy module
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """this function is for executing this the code for
    fetching first row from states table"""
    args = sys.argv[1:]
    passwrd = args[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    states = session.query(State).filter_by(id=1)
    print(f"{states[0].id}: {states[0].name}")


if __name__ == '__main__':
    main()
