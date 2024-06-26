#!/usr/bin/python3
"""This module handles the storage of HBNB objects"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    
    storage = DBStorage()
else:
   
    storage = FileStorage()

storage.reload()
