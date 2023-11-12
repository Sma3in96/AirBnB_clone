#!/usr/bin/python3
""" creating cmd interpreter """
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """class of hbnb prompt """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
