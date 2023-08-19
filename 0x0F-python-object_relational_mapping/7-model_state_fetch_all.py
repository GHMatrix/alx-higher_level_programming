#!/usr/bin/python3

"""Lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function"""
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        return

    username, password, database = argv[1], argv[2], argv[3]
    connection_url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
