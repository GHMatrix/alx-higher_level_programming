#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define the State class using SQLAlchemy
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a declarative base
    Base = declarative_base()

    # Create the table in the database
    Base.metadata.create_all(engine)
