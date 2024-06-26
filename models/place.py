#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

# Association table for the many-to-many relationship between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equal to current Place.id"""
            from models.review import Review  # Import locally to avoid circular import
            from models import storage  # Import inside the property to avoid circular import
            all_reviews = storage.all(Review)
            place_reviews = [review for review in all_reviews.values() if review.place_id == self.id]
            return place_reviews

        @property
        def amenities(self):
            """Returns the list of Amenity instances linked to the Place"""
            from models.amenity import Amenity  # Import locally to avoid circular import
            from models import storage  # Import inside the property to avoid circular import
            all_amenities = storage.all(Amenity)
            place_amenities = [amenity for amenity in all_amenities.values() if amenity.id in self.amenity_ids]
            return place_amenities

        @amenities.setter
        def amenities(self, amenity_obj):
            """Adds an Amenity to the amenity_ids list"""
            from models.amenity import Amenity  # Import locally to avoid circular import
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
    
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
