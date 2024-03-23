#!/usr/bin/python3
"""State Module for HBNB project """


from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
            Getter attribute that returns the returns
            the list of City instances with
            state_id equals to the current State.id.
            """
            list_of_city = []
            for city in models.storage.all(models.City).values():
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city
