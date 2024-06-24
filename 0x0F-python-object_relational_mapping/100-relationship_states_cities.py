#!/usr/local/bin/python3

"""
    this module is for adding one state and one city
    and linking them with each other
"""
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """this function is for addting one state and one city
        and linking them with each other
    """

    args = sys.argv[1:]
    passwrd = args[1]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[0], passwrd, args[2]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    state = State(name='California')
    session.add(state)
    session.commit()

    new_city = City(state_id=state.id, name='San Francisco')
    session.add(new_city)
    session.commit()


if __name__ == '__main__':
    """execute main function"""
    main()