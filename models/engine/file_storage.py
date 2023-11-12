#!/usr/bin/python3
""" file storage class creating """
import json
import os


class FileStorage:
    """class of FileStorage"""
    __file_path = "store.json"
    __objects = {}

    def new(self, obj):
        """methode that create a new obj"""
        k = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[k] = obj

    def all(self):
        """ return all objects"""
        return FileStorage.__objects

    def save(self):
        """ save the objects into a json"""
        temp_dict = {}

        for k, v in FileStorage.__objects.items():
            temp_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as file_open:
            json.dump(temp_dict, file_open)

    def reload(self):
        """ reload a object"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        dct_class = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                     'City': City, 'Amenity': Amenity, 'State': State,
                     'Review': Review}
        file_path = FileStorage.__file_path

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    instance = dct_class[class_name](**value)
                    self.new(instance)
