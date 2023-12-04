#!/usr/bin/python3
# BaseModel defines all common attributes/methods for other classes

import uuid
from datetime import datetime


class BaseModel:
    """ base model """
    def __init__(self, *args, **kwargs):
        """ init methode """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            dateformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(kwargs[key], dateformat)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ str methode """
        name_of_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)

    def save(self):
        """ save methode """
        from models.engine.file_storage import FileStorage
        self.updated_at = datetime.now()
        storage = FileStorage()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ to dict methode """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
