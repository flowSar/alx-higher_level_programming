#!/usr/local/bin/python3

"""
    this module is for query data from two tables that have
    a relationship with ech other
"""
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload, relationship
import sys


def main():
    """
        this module is for query data from two tables that have
        a relationship and print this data
    """
    args = sys.argv[1:]
    user = args[0]
    passwd = args[1]
    db = args[2]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db))

    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    states = session.query(State).options(joinedload(State.cities)).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == '__main__':
    main()
