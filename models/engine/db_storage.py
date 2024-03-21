#!/usr/bin/python3
"""Python Interpreter."""


import models
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User
import os


my_classes = {"City": City, "Place": Place, "Review": Review,
              "State": State, "Amenity": Amenity, "USer": User}


class DBStorage:
    """Instantiates a class DBStorage."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage instance."""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        # Creates the angine and connects it to the database
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    user, passwd, host, db), pool_pre_ping=True)

        # Drops all the tables if the env variable is equal to test.
        if os.getenv('HBNB_ENV') == 'test':
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

            if cls is None:
                for my_class in my_classes:
                    objects = self.__session.query(my_class).all()
                    for obj in objects:
                        objects_dict[obj] = obj
            else:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    objects_dict[obj] = obj

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

        def reload(self):
            """Creates all tables in the database."""
            Base.metadat.create_all(self.__engine)

            # Create a session factory
            Session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)

            # Create a database Session and make it thread-safe
            Session = scoped_session(Session_factory)
            self.__session = Session()
