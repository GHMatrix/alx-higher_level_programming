#!/usr/bin/python3

""" Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_id_by_name(username, password, database, state_name):
    """ Find and print the State's id by its name """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} username password database state_name"
              .format(argv[0]))
        exit(1)

    find_state_id_by_name(argv[1], argv[2], argv[3], argv[4])
