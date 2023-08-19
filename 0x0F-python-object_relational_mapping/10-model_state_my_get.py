#!/usr/bin/python3

"""
Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def find_state_id(username, password, database, state_name):
    """Finds and prints the state id"""
    connection_url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    find_state_id(username, password, database, state_name)
