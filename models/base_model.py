#!/usr/bin/python3

# imports
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    A class that defines all common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        public instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                # if kwargs is not empty, set attr from kwargs
                if key != '__class__':
                    # convert string dates back to datetime objects
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """
        print str repr of the object
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
