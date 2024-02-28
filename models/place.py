#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)

class Place(BaseModel, Base):
    """ Place inherits from BaseModel and Base and a nice place to stay. """
    __tablename__ = 'places'
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        return [amenity for amenity in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
    
    def __init__(self, *args, **kwargs):
        # Initialize other attributes
        self.amenity_ids = []
    
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

