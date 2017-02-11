#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """ Place Class

    Holds thirteen public attributes: 'city_id', 'user_id', 'name',
    'description', 'number_rooms', 'number_bathrooms', 'max_guest',
    'price_by_night', 'number_rooms', 'latitude', 'longitude', 'amentities'.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    number_rooms = 0
    latitude = 0.0
    longitude = 0.0
    amentities = ""

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
