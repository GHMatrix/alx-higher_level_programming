"""
This module defines SQLAlchemy ORM classes for the states and cities tables.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the states table.

    Attributes:
        id (int): Primary key ID of the state.
        name (str): Name of the state.
        cities (relationship): One-to-many relationship with City objects.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    cities = relationship("City", backref="state", order_by="City.id")


class City(Base):
    """
    Represents a city in the cities table.

    Attributes:
        id (int): Primary key ID of the city.
        state_id (int): Foreign key ID referencing the parent State.
        name (str): Name of the city.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(256), nullable=False)
