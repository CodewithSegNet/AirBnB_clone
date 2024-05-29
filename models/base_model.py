#!/usr/bin/env python3

# imports
from datetime import datetime
import uuid



class BaseModel:
    """
    a class that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            # if kwargs is not empty, set attributes from kwargs
            for key, value in kwargs.items():
                if key != '__class__':
                    # convert string dates back to datetime objects
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:            
            # Default initialization
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # import storage
            from models import storage
            storage.new(self)

    def __str__(self):
        # Return a string representation of the instance
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        # Update the updated_at attribute to the current datetime
        self.updated_at = datetime.now()
        # import storage
        from models import storage
        storage.save()

    @classmethod
    def count(cls):
        """Returns the number of instances of the class"""
        return len(cls.all())

    def to_dict(self):
        # Create a copy of the instance's dictionary of attributes
        dict_repr = self.__dict__.copy()
        # Add the class name to the dictionary representation
        dict_repr['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

