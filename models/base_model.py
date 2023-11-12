#!/usr/bin/python3
# BaseModel defines all common attributes/methods for other classes
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ base model """
    def __init__(self, *args, **kwargs):
        """ init methode """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            dateformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(kwargs[key], dateformat)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ str methode """
        temp_dict = {}
        for key, value in self.__dict__.items():
            if (not value) is False:
                temp_dict[key] = value
        A = str(temp_dict)
        B = "[" + self.__class__.__name__ + "]"
        return B + " (" + self.id + ")" + A

    def save(self):
        """ save methode """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to dict methode """
        temp_dict2 = {}
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        for k, v in self.__dict__.items():
            if k == 'updated_at' or k == 'created_at':
                temp_dict2[k] = v.strftime(dateformat)
            elif v:
                temp_dict2[k] = v
        temp_dict2['__class__'] = self.__class__.__name__
        return temp_dict2
