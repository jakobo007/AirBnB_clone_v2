#!/usr/bin/python3
"""This module handles the storage of HBNB objects"""

from os import getenv
from models.engine.db_storage import DBStorage

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    #from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    #from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
