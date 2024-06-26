#!/usr/bin/python3
"""this module is for connecting to mysql database
    and and updating the state name
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        this function if for updating the state name to a new name
    """
    args = sys.argv[1:]
    passwrd = args[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    new_state = State(name='Louisiana')
    session = sessionmaker(bind=engine)()
    updated_state = session.query(State).filter_by(id=2).first()
    if updated_state:
        updated_state.name = 'New Mexico'
        session.commit()


if __name__ == '__main__':
    """execute main"""
    main()
