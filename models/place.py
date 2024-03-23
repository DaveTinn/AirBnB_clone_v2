#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_amenity', String(60), ForeignKey('places.id'),
            nullable=False, primary_key=True),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", passive_deletes=True, backref="place")
        amenities = relationship(
                "Amenity", secondary=place_amenity,
                back_populates="place_amenities", viewonly-False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """
        Getter attribute that returns the list of Review instances
        with place_id equals to the current Place.id.
        """
        from models.review import Review
        list_of_review = []
        reviews = models.storage.all(Review)
        for review in reviews.value():
            if review.place_id == self.id:
                list_of_review.append(review)
        return list_of_review

    @property
    def amenities(self):
        """
        Returns the list of Amenity instances based on
        the attribute amenity_ids that contains all Amenity.id linked to Place.
        """
        from models.amenity import Amenity
        list_of_amenity = []
        amenities = models.storage.all(Amenity)
        for amenity in amenities.value():
            if amenity.id in amenity_ids:
                list_of_amenity.append(amenity)
        return list_of_amenity

    @property
    def amenities(self, obj=None):
        """
        Handles the append method for adding Amenity.id
        to attribute amenity.ids.
        """
        if obj and isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
