#!/usr/bin/python3
"""
This module defines SQLAlchemy ORM classes for the cities table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
