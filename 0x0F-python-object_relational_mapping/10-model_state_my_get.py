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
    """
        this function if for querying data from table states based on
        constrint we set: in this case with same the name
        and by using sqlalchemy instead or raw SQL.
    """
    args = sys.argv[1:]
    passwrd = args[1]
    state_name = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name == state_name).all()
    if states:
        print(f"{states[0].id}")
    else:
        print('Not found')


if __name__ == '__main__':
    """execute main"""
    main()
