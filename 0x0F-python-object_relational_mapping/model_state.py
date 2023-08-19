#!/usr/bin/python3

"""
Module to define the State class
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

class State(Base):
    """
    State class representing the 'states' table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

    # Create the 'states' table
    Base.metadata.create_all(engine)
