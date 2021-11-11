#!/usr/bin/python3
"""More Project Classes"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that unheriths"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
