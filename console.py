#!/usr/bin/python3
""" creating cmd interpreter """
import cmd
import sys
"""from models.base_model import BaseModel
import json"""


class HBNBCommand(cmd.Cmd):
    """class of hbnb prompt """

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


if __name__ == '__main__':
    if sys.stdin.isatty():
        HBNBCommand.prompt = "(HBNB) "
    else:
        HBNBCommand.prompt = ""
    HBNBCommand().cmdloop()
