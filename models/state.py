#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """ State Class

    Holds one public attribute: 'name'.
    """

    name = ""

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
