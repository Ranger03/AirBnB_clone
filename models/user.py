#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        mail (str): email of the user.
        pwd (str): password of the user.
        first_name (str): first name of user.
        last_name (str):  last name of  user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
