#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review Class

    Holds three public attributes: 'place_id', 'user_id', 'text'.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
