#!/usr/bin/env python3

from models.base_model import BaseModel

class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    @classmethod
    def count(cls):
        """Returns the number of instances of the class"""
        return len(cls.all())
        