#!/usr/bin/python3
"""this module is for connecting to mysql database
    and and inserting new state to states table
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    new_state = State(name='Louisiana')
    session = sessionmaker(bind=engine)()
    session.add(new_state)
    session.commit()


if __name__ == '__main__':
    """execute main"""
    main()
