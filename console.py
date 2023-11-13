#!/usr/bin/python3
""" creating cmd interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
"""import json"""


class HBNBCommand(cmd.Cmd):
    """class of hbnb prompt """

    prompt = "(hbnb) "
    __dict_class = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                    'City': City, 'Place': Place,
                    'Review': Review, 'State': State}

    def help_help(self, line):
        """helps u on help"""
        print("Provides description of a given command")

    def emptyline(self):
        """ empty line entered"""
        pass

    def do_quit(self, line):
        """quit the console"""
        return True

    def do_EOF(self, line):
        """end of file"""
        print()
        return True

    def do_show(self, line):
        """show methode"""
        arg = line.split()
        objec_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__dict_class.key():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objec_dict:
            print("** no instance found **")
        else:
            print(objec_dict["{}.{}".format(arg[0], arg[1])])

    def do_count(self, cls_name):
        """count"""
        counter = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == cls_name:
                counter = counter + 1
        print(counter)

    def do_create(self, classins):
        """ Creates an instance according to a given class """

        if not classins:
            print("** class name missing **")
        elif classins not in HBNBCommand.__dict_class.keys():
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.__dict_class[classins]()
            print(my_model.id)
            my_model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
