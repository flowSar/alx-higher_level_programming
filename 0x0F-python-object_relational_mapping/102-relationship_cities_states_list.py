#!/usr/local/bin/python3

"""
    this module is for query data from two tables that have
    a relationship with ech other
"""
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import sys


def main():
    """
        this module is for query data from  two tables that have
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
    cities = session.query(City).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()


if __name__ == '__main__':
    main()
