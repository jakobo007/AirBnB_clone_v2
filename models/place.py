from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)  # Allow NULL values for description
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)  # Allow NULL values for latitude
    longitude = Column(Float, nullable=True)  # Allow NULL values for longitude
    amenity_ids = []  # This should be handled separately

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


