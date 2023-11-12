#!/usr/bin/python3
""" create user sub-class"""
from models.base_model import BaseModel


class user(BaseModel):
    """user sub - class definition """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
