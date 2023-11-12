#!/usr/bin/python3
""" file storage class creating """
import json
import os


class FileStorage:
    __file_chemin = "store.json"
    __dict_obj = {}

    def new(self, obj):
        k = obj.__class__.__name__ + "." + obj.id
        FileStorage.__dict_obj[k] = obj

    def all(self):
        return FileStorage.__dict_obj

    def save(self):
        temp_dict = {}

        for k, v in FileStorage.__dict_obj.items():
            temp_dict[k] = v.to_dict()
        with open(FileStorage.__file_chemin, 'w') as file_open:
            json.dump(temp_dict, file_open)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        dct_class = {'BaseModel': BaseModel, 'User': User}
        file_path = FileStorage.__file_path

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    instance = dct_class[class_name](**value)
                    self.new(instance)
