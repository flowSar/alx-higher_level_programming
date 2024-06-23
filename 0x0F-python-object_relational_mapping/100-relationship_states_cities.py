#!/usr/bin/python3

"""
    this module is for adding one state and one city
    and linking them with each other
"""
from model_city import Base, City
from model_state import State
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
    city = City(name='San Francisco', state_id=1)
    session.add(state)
    session.add(city)
    session.commit()


if __name__ == '__main__':
    """execute main function"""
    main()
