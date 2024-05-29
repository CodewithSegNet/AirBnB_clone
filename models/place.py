#!/usr/bin/env python3

from models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = 0
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_nigth = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    @classmethod
    def count(cls):
        """Returns the number of instances of the class"""
        return len(cls.all())