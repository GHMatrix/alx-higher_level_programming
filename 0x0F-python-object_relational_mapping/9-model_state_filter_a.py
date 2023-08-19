#!/usr/bin/python3

"""Lists all State objects that contain the letter 'a'
   from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]
    connection_url = (
        f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states_with_a = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
        )
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
