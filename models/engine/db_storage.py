#!/usr/bin/python3
"""Python Interpreter."""


import models
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User
from os import getenv
import sqlalchemy


classes = {"City": City, "Place": Place, "Review": Review,
           "State": State, "Amenity": Amenity, "USer": User}


class DBStorage:
    """Instantiates a class DBStorage."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage instance."""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        # Creates the angine and connects it to the database
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, passwd, host, db), pool_pre_ping=True)

        # Drops all the tables if the env variable is equal to test.
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Initializes an instance of the DBStorage

        Arguments:
            cls: The class type of the objects.

        Returns:
            A dictionary of the objects in the storage.
        """
        objects_dict = {}

        for my_cls in my_classes:
            if cls is None or cl is classes[my_cls] or cls is my_cls:
                my_obj = self.__session.query(classes[my_cls]).all()
                for my_obj in objects:
                    key = my_obj.__class__.__name__ + '_' + my_obj.id
                    objects_dict[key] = my_obj
        return objects_dict

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add()

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates all tables in the database."""
        Base.metadata.create_all(self.__engine)

        # Create a session factory
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        # Create a database Session and make it thread-safe
        Session = scoped_session(Session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session."""
        if self.__session:
            sef.__session.close()
