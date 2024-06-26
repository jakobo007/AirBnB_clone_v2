#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances with state_id equals to the current State.id"""
        city_list = []
        for city in models.storage.all(models.City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
        