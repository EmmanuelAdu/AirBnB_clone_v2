#!/usr/bin/python3
"""New DB Storage for mysql
"""
from os import getenv
from sqlalchemy import create_engine, MetaData


class DBStorage():
    """Represents class storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """Returns a dict of all objects depending
        on class name `cls`
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = [
                State,
                City,
                User,
                Place,
                Review,
                Amenity
        ]

        rows = []

        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """Add a new object `obj` to the database"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """Commit changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from database"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in db"""
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        from models.place import Place
        from sqlalchemy.orm import sessionmaker, scoped_session

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__session)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove method on the private session method"""
        self.__session.remove()
