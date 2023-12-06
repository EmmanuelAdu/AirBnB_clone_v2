#!/usr/bin/python3
"""This module initializes the storage package"""
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")
if storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
