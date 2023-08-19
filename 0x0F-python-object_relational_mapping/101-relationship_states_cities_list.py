#!/usr/bin/python3

"""
Script to list all State objects and their corresponding
City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City


def list_states_and_cities(username, password, database):
    """ List all State objects and their corresponding City objects """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State).order_by(State.id).all()

    for state in states_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    list_states_and_cities(argv[1], argv[2], argv[3])
