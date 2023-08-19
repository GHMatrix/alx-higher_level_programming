#!/usr/bin/python3

"""Prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]
    connection_url =
    f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        first_state = session.query(State).order_by(State.id).first()
        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")
