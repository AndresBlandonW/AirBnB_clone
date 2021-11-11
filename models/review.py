#!/usr/bin/python3
"""More Project Classes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class of review information for units in HolBnb
    """
    place_id = ""
    user_id = ""
    text = ""
