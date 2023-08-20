#!/usr/bin/python3
""" Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database using SQLAlchemy and retrieve the required data
    result = session.query(State).order_by(State.id).all()

    # Print the results in the desired format
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
