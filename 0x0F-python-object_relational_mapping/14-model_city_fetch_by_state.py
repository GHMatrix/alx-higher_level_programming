#!/usr/bin/python3

"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """Fetches and prints all City objects by state"""
    connection_url = (
            f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        cities = (
            session.query(State, City)
            .filter(State.id == City.state_id)
            .all()
        )
        for state, city in cities:
            print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_cities_by_state(username, password, database)
