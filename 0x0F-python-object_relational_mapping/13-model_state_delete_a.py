#!/usr/bin/python3
"""this module is for connecting to mysql database
    and and deleting all the states with name containing
    'a'
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
        this function if fordeleting all the states
        with name containing 'a'
    """
    args = sys.argv[1:]
    passwrd = args[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd,
                                   args[2]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    new_state = State(name='Louisiana')
    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.name.like('%a%')).all()
    if states:
        for state in states:
            session.delete(state)
            session.commit()


if __name__ == '__main__':
    """execute main"""
    main()
