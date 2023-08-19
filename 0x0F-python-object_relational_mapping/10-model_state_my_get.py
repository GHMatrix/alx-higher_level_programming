#!/usr/bin/python3

""" Prints the State object with the name passed as an argument
    from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database,
    state_name = argv[1], argv[2], argv[3], argv[4]

    connection_url = "mysql+mysqldb://{}:{}@localhost/{}"
    .format(username, password, database)
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")
