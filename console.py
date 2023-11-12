#!/usr/bin/python3
""" creating cmd interpreter """
import cmd
"""from models.base_model import BaseModel
import json"""


class HBNBCommand(cmd.Cmd):
    """class of hbnb prompt """

    def help_help(self):
        """helps u on help"""
        print("Provides description of a given command")

    def emptyline(self):
        """ empty line entered"""
        pass

    def do_quit(self):
        """quit the console"""
        return True

    def do_EOF(self):
        """end of file"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
