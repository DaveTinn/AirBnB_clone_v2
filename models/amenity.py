#!/usr/bin/python3
""" Amenity Module for HBNB project """


from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
import models


class Amenity(BaseModel):
    """Defines the class Amenity that inherits from BaseModel and Base."""

    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""
