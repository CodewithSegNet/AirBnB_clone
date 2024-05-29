#!/usr/bin/env python3

from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.text = ""