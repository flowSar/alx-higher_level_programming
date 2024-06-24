#!/usr/bin/python3

"""
    this module is for query data from two tables that have
    a relationship with ech other
"""
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = session.query(City).filter(state.id == City.state_id).all()
        for city in cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == '__main__':
    main()
