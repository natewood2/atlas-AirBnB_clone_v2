#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
STO_TYP = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if STO_TYP == "db":
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''
