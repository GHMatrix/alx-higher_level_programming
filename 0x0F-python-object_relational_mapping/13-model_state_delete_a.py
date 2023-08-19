#!/usr/bin/python3

"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """Deletes states with a name containing 'a'"""
    connection_url = (
            f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    )
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        states_with_a = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .all()
        )
        for state in states_with_a:
            session.delete(state)
        session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    delete_states_with_a(username, password, database)
