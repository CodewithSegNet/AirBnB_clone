#!/usr/bin/env python3

from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    
    def __init__(self, *args, **kwargs):
        """Constructor method for User class"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    @classmethod
    def count(cls):
        """Returns the number of instances of the class"""
        return len(cls.all())