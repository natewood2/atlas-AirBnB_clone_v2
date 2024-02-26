#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            time_now = datetime.utcnow()
            if 'created_at' not in kwargs:
                self.created_at = time_now
            if 'updated_at' not in kwargs:
                self.updated_at = time_now

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current storage instance"""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        data['__class__'] = self.__class__.__name__
        return data
