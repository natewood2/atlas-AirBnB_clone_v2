#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone
with new SQL database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
import os


class DBStorage:
    """
    Handles long-term storage of all class instances via SQLAlchemy ORM.
    Thank you Doug.
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the database engine. """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries all objects of a given class from the database. """
        objects = {} 
        if cls:
            query = self.__session.query(cls).options(joinedload('*')).all()
            for obj in query:
                key = f'{type(obj).__name__}.{obj.id}'
                objects[key] = obj
        else:
            for cls in Base._decl_class_registry.values():
                if hasattr(cls, '__tablename__'):  # Filter out non-table classes
                    query = self.__session.query(cls).options(joinedload('*')).all()
                    for obj in query:
                        key = f'{type(obj).__name__}.{obj.id}'
                        objects[key] = obj
        return objects

    def new(self, obj):
        """ Adds a new object to the session. """
        self.__session.add(obj)

    def save(self):
        """ Commits changes to the database. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the session. """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates database tables and initializes a new session. """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()