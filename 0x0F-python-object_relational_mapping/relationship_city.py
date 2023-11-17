#!/usr/bin/python3
"""
A python file that contains the class definition of a city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from relationship_state import Base, State


class City(Base):
    """
    defining the city class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
