#!/usr/bin/python3

"""
Script to list all State objects and their corresponding City
objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City


def list_states_and_cities(username, password, database):
    """ List all State objects and their corresponding City objects """
    connection_url = (
            f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State).order_by(State.id).all()

    for state in states_and_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} username password database")
        exit(1)

    list_states_and_cities(argv[1], argv[2], argv[3])
